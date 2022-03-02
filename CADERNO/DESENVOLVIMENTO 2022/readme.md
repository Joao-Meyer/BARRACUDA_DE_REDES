# Criação de aplicação full stack

## BACKEND com NODE JS

+ Instalar o node

+ Inicializar o node na pasta do projeto
> npm init

+ Instalar pacotes que serão utilizados:
express para o servidor e rotas
> npm i express

nodemon para atualização automática do servidor ao editar e salvar um arquivo
> npm i nodemon -D

sequelize para a conexão e operação do DB
> npm i sequelize

sequelize-cli para rodar comandos do terminal
> npm i sequelize-cli -D

mysql2 para utilização do MySQL
> npm i mysql2

jest para testes ( utilizado para testar a API, também, durante o desenvolvimento )
> npm i jest

cross-fecth para auxiliar nos testes de endpoints da api
> npm i cross-fetch

Obs: Posteriormente substituir pelo supertest e o cross-env para testes mais robustos ( https://www.youtube.com/watch?v=B1kWb7tWoxs&t=2s&ab_channel=RafaelLeme )

jsonwebtoken para autenticação de usuários
> npm i jsonwebtoken

+ Criar o servidor e a aplicação

dentro de src adicionar os arquivos:

app.js
```
const express = require('express');

const server = express();

server.use(express.json());

module.exports = server;
```

routes.js
```
const express = require('express');

const routes = express.Router();

routes.get('/', (req, res) => {
    return res.json({
        statusRes : "ok",
        message : "Tudo certo."
    })
})

module.exports = routes;
```

index.js
```
const app = require('./app');
const routes = require('./routes');

const port = 3000;

app.use(routes);

app.listen(port, () => console.log(`Servidor rodando na porta ${port}`));
```

Adicionar o script de testes para verificar se a API sobe normalmente

dentro de src/tests:

api.test.js
```
const fetch = require('cross-fetch');

const baseUrl = 'http://localhost:3000';

describe('API', () => {
    test('API está de pé.', async() => {
        const response = await fetch( baseUrl );

        const responseBody = await response.json();

        expect( response.status ).toBe( 200 );
        expect( responseBody.statusRes ).toBe( 'ok' )
    })
})
```

Adicionar os scripts do servidor e de teste dentro do package.json:
```
//...
"scripts": {
    "test": "jest",
    "dev": "nodemon ./src/index.js"
},
//...
```

Iniciar o servidor e rodar o teste:
> npm run dev
> npm run test

## BANCO DE DADOS + BACKEND

+ Criar uma pasta database e uma pasta config dentro de src

dentro de config:

database.js
```
module.exports = {
    dialect : "mysql",
    host : "localhost",
    username : "root",
    password : "a1s2d3f4",
    database : "treino_prova",
    logging: console.log,
    define : {
        timestamp : true,
        underscored : true
    }
}
```

dentro da pasta database:

index.js
```
const Sequelize = require('sequelize');
const dbConfig = require('../config/database');

const connection = new Sequelize(dbConfig);

module.exports = connection;
```

+ Importar o database dentro do 'servidor':

index.js
```
const app = require('./app');
const routes = require('./routes');

require('./database');

const port = 3000;

app.use(routes);

app.listen(port, () => console.log(`Servidor rodando na porta ${port}`));
```

+ Criar um arquivo na raiz do projeto .sequelizerc para indicar onde estão as configurações que fizemos do sequelize

.sequelizerc
```
const path = require("path");

module.exports = {
    config : path.resolve(__dirname, 'src', 'config', 'database.js'),
};
```

E podemos criar o DB que foi especificado na config rodando:
> npx sequelize db:create

+ Adicionar uma pasta onde ficarão as migrations dentro de src/database chamada migrations e adicionar seu endereço no .sequelizerc:

.sequelizerc
```
const path = require("path");

module.exports = {
    config : path.resolve(__dirname, 'src', 'config', 'database.js'),
    'migrations-path' : path.resolve(__dirname, 'src', 'database', 'migrations')
};
```

+ Criar as migrations utilizando o comando base:
> npx sequelize migration:create --name=create-table_name

O conteúdo da migration deve ser aproximadamente este:

20220301135943-create-table_name
```
'use strict';

module.exports = {
  async up (queryInterface, Sequelize) {
    /**
     * Add altering commands here.
     *
     * Example:
     * await queryInterface.createTable('users', { id: Sequelize.INTEGER });
     */
  },

  async down (queryInterface, Sequelize) {
    /**
     * Add reverting commands here.
     *
     * Example:
     * await queryInterface.dropTable('users');
     */
  }
};
```

Um exemplo de migration seria:

20220301170101-create-users.js
```
'use strict';

module.exports = {
  async up (queryInterface, Sequelize) {    
    await queryInterface.createTable('users', {
      id : {
        type : Sequelize.INTEGER,
        primaryKey : true,
        autoIncrement : true,
        allowNull : false,
      },
      name : {
        type : Sequelize.STRING,
        allowNull : false,
      },
      email : {
        type : Sequelize.STRING,
        allowNull : false,
      },
      password : {
        type : Sequelize.STRING,
        allowNull : false,
      },
      created_at : {
        type : Sequelize.DATE,
        allowNull : false,
      },
      updated_at : {
        type : Sequelize.DATE,
        allowNull : false,
      },
    });
  },

  async down (queryInterface, Sequelize) {
    
    await queryInterface.dropTable('users');
     
  }
};
```

+ Criar as tabelas rodando o comando:
> npx sequelize db:migrate

Obs: Caso queira desfazer as alterações do migrate, rodar o comando ( desfaz apenas a última migration ):
> npx sequelize db:migrate:undo

+ Adicionar a pasta models dentro de src

Exemplo de model:

User.js
```
const { Model, DataTypes } = require('sequelize');

class User extends Model {
    static init(sequelize) {
        super.init({
            name : DataTypes.STRING,
            email : DataTypes.STRING,
            password : DataTypes.STRING
        }, {
            sequelize
        })
    }
}

module.exports = User;
```

+ Adicionamos as models dentro do index.js do database:

index.js
```
const Sequelize = require('sequelize');
const dbConfig = require('../config/database');

const User = require('../models/User');

const connection = new Sequelize(dbConfig);

User.init(connection);

module.exports = connection;
```

+ Criamos uma pasta chamada controllers dentro de src

Exemplo de controller:

UserController.js
```
const User = require('../models/User');

module.exports = {
    async store(req, res){
        const { name, email, password } = req.body;

        const user = await User.create({ name, email, password });
        
        return res.status(201).json( user );
    }
};
```

+ Importamos os controllers e utilizamos seus métodos nos endpoints:

routes.js
```
const express = require('express');

const UserController = require('./Controllers/UserController');

const routes = express.Router();

routes.get('/', (req, res) => {
    return res.json({
        statusRes : "ok",
        message : "Tudo certo."
    })
})

routes.post('/users', UserController.store);

module.exports = routes;
```

+ Testar adicionando um teste

api.test.js
```
const fetch = require('cross-fetch');

const baseUrl = 'http://localhost:3000/';

describe('API', () => {
    test('API está de pé.', async() => {
        const response = await fetch( baseUrl );

        const responseBody = await response.json();

        expect( response.status ).toBe( 200 );
        expect( responseBody.statusRes ).toBe( 'ok' )
    });

    test('É possível criar um usuário.', async() => {
        const newUser = {
            name : 'Johnny Test',
            email : 'jtest@mail.com',
            password : 's3cr3t!'
        };

        const response = await fetch( baseUrl + 'users', {
            method: "post",
            headers: {
              'Accept': 'application/json',
              'Content-Type': 'application/json'
            },
            body: JSON.stringify(newUser)
        });

        const responseBody = await response.json();

        expect( response.status ).toBe( 201 );
        expect( responseBody.name ).toBe( newUser.name );
    });
});
```

## Implementando JWT para autenticação no BACKEND

+ Adição de um arquivo que vai conter a string chave dentro da pasta src/config

auth.json
```
{
    "secret" : "treinoProva",
    "expires" : 300
}
```

+ Utilização do jsonwebtoken

Exemplo na controller de Sessão:

SessionController.js
```
const User = require('../models/User');
const jwt = require('jsonwebtoken');
const authConfig = require('../config/auth.json')

module.exports = {
    async login(req, res){
        const { email, password } = req.body;

        const user = await User.findOne({
            where: {
                email,
                password
            }
        });
    
        if( !user ){
            return res.status( 401 ).send({ erro : "E-mail e/ou senha incorretos." });
        }

        const token = jwt.sign({ userId: user.id }, authConfig.secret, { expiresIn: authConfig.expires });

        res.status(201).send({
            auth: true,
            user: {
                userId: user.id,
                name: user.nome,
                email: user.email
            },
            token
        });
    }
};
```

Teste automatizado para verificar se está funcional o login:

api.test.js
```
//...
    test('Login está funcionando.', async () => {
        const userWithoutAccess = {
            email: 'user@example.com',
            password: 'password'
        };

        const userWithAccess = {
            email : 'jtest@mail.com',
            password : 's3cr3t!'
        };

        const responseWithFail = await fetch( baseUrl + 'login', {
            method: "post",
            headers: {
              'Accept': 'application/json',
              'Content-Type': 'application/json'
            },
            body: JSON.stringify(userWithoutAccess)
        });

        const responseBodyWithFail = await responseWithFail.json();

        expect( responseWithFail.status ).toBe( 401 );
        expect( JSON.stringify(responseBodyWithFail) ).toContain( 'erro' );
        
        const responseWithSuccess = await fetch( baseUrl + 'login', {
            method: "post",
            headers: {
              'Accept': 'application/json',
              'Content-Type': 'application/json'
            },
            body: JSON.stringify(userWithAccess)
        });

        const responseBodyWithSucces = await responseWithSuccess.json();

        expect( responseWithSuccess.status ).toBe( 201 );
        expect( JSON.stringify(responseBodyWithSucces) ).toContain( 'token' );
    })
//...
```

+ Ao adicionar o jwt é possível o controle sessão e acesso às rotas adicionando um middleware

Criar a pasta middlewares dentro de src com o arquivo authorization.js

authorization.js
```
const jwt = require('jsonwebtoken');
const authConfig = require('../config/auth.json');

module.exports = ( req, res, next ) => {
    const token = req.headers['x-access-token'];

    if(!token){
        res.status(401).send({ erro : "Token mal formatado." })
    }

    try {
        const retorno = jwt.verify(token, authConfig.secret);

        req.userId = retorno.userId;

        return next();
    } catch (error) {
        return res.status(401).send({ erro : "Token inválido." })
    }
}
```

Adicionando o middleware antes das rotas privadas no arquivo de routes:

routes.js
```
const express = require('express');
const authorizationMiddleware = require('./middlewares/authorization');

const UserController = require('./Controllers/UserController');
const SessionController = require('./Controllers/SessionController')

const routes = express.Router();

routes.get('/', (req, res) => {
    return res.json({
        statusRes : "ok",
        message : "Tudo certo."
    })
})

routes.post('/login', SessionController.login)

routes.post('/users', UserController.store);

routes.use(authorizationMiddleware);

// Rotas a partir daqui se tornam privadas e acessíveis apenas com token de autenticação

module.exports = routes;
```

+ Teste para verificar se a autorização está funcional

Criar uma rota que liste os usuários que será privada:

UserController.js
```
const User = require('../models/User');

module.exports = {
    async store(req, res){
        const { name, email, password } = req.body;

        const user = await User.create({ name, email, password });
        
        return res.status(201).json( user );
    },

    async index(req, res){
        const users = await User.findAll();
        
        return res.status(200).json( users );
    },
};
```

routes.js
```
const express = require('express');
const authorizationMiddleware = require('./middlewares/authorization');

const UserController = require('./Controllers/UserController');
const SessionController = require('./Controllers/SessionController')

const routes = express.Router();

routes.get('/', (req, res) => {
    return res.json({
        statusRes : "ok",
        message : "Tudo certo."
    })
})

routes.post('/login', SessionController.login)

routes.post('/users', UserController.store);

routes.use(authorizationMiddleware);

routes.get('/users', UserController.index);

module.exports = routes;
```

api.test.js
```
//...
    test('Apenas usuários logados estão podendo listar todos os usuários.', async () => {        
        const userWithAccess = {
            email : 'jtest@mail.com',
            password : 's3cr3t!'
        };
        
        const responseLogin = await fetch( baseUrl + 'login', {
            method: "post",
            headers: {
              'Accept': 'application/json',
              'Content-Type': 'application/json'
            },
            body: JSON.stringify(userWithAccess)
        });

        const responseBodyLogin = await responseLogin.json();

        expect( responseLogin.status ).toBe( 201 );
        expect( responseBodyLogin ).toHaveProperty( 'token' );

        const token = responseBodyLogin.token;

        const responseWithoutToken = await fetch( baseUrl + 'users' );
        const responseBodyWithoutToken = await responseWithoutToken.json();

        expect( responseWithoutToken.status ).toBe( 401 );
        expect( responseBodyWithoutToken ).toHaveProperty( 'erro' );

        const responseWithToken = await fetch( baseUrl + 'users', {
            headers: {
              'x-access-token': token,
            }
        });

        expect( responseWithToken.ok ).toBeTruthy();
    })
//...
```

