# Caderno de anotações

## Preparando o ambiente de trabalho
Foram utilizados diferentes recursos para o desenvolvimento desta aplicação, como:
A ferramenta VISUAL STUDIO CODE, para escrever códigos e auxiliar em vários momentos como interface para instalações e melhor visualização de trechos específicos.<br>
- Pode ser instalada a partir de um executável encontrada na página <https://code.visualstudio.com/>

A ferramenta POSTMAN, para o teste de requisições HTTP.<br>
- Pode ser instalada a partir de um executável encontrada na página <https://www.postman.com/downloads/>

O banco de dados MYSQL, para armazenar informações da aplicação.<br>
- Pode ser instalado a partir da página <https://www.mysql.com/downloads/>

A ferramenta MYSQL WORKBENCH, para manipular o MYSQL com maior facilidade.<br>
- Pode ser instalado a partir de um executável encontrada na página <https://www.mysql.com/downloads/>

A tecnologia NODE, para poder fazer diversas funções do backend.<br>
- Pode ser instalada a partir de um executável encontrada na página <https://nodejs.org/en/>

A biblioteca NODEMON, para agilizar o processo de subir a aplicação.<br>
- Pode ser instalado a partir do comando:<br>
> 
```
npm install nodemon -D
```

O ORM SEQUELIZE
- Pode ser instalado a partir do comando:<br>
> 
```
npm install sequelize
```

O framework EXPRESS
- Pode ser instalado a partir do comando:<br>
>
```
npm install express
```

O framework para utilização do MYSQL
- Pode ser instalado a partir do comando:<br>
>
```
npm install mysql2
```

O cliente do ORM SEQUELIZE, para interação com o banco de dados MYSQL.<br>
- Pode ser instalado a partir do comando:<br>
>
```
npm install sequelize-cli -D
```

## Iniciando o projeto
Primeiro é necessário criar um "esqueleto" para que o projeto possa ao menos executar, e para tal criamos o "app" por meio do EXPRESS.
Nós implementamos da seguinte maneira:
>
```javascript
const express = require('express');

// Iniciando a aplicação
const app = express();

// Exportar a aplicação configurada
module.exports = app;
```

Porém até então ele não faz nada além de começar a executar, então criamos um "server" para poder subir a aplicação.
```javascript
const app = require('./app.js');

const porta = 3333;

// Sobe a aplicação em um servidor(conteiner)
app.listen(porta, () => {
    console.log(`Servidor rodando na porta ${porta}.`);
});
```
E com isso a aplicação já está subindo.

## Criando o banco de dados

Por meio do SEQUELIZE é possível criar o banco de dados e também manipular.

Primeiro é necessário conectar ao database, para poder prosseguir foi consultada a documentação oficial do SEQUELIZE em <https://sequelize.org/master/manual/getting-started.html>.

Para conectar ao database foi usado o seguinte trecho de código como base:
> 
```javascript
const { Sequelize } = require('sequelize');

// Option 1: Passing a connection URI
const sequelize = new Sequelize('sqlite::memory:') // Example for sqlite
const sequelize = new Sequelize('postgres://user:pass@example.com:5432/dbname') // Example for postgres

// Option 2: Passing parameters separately (sqlite)
const sequelize = new Sequelize({
  dialect: 'sqlite',
  storage: 'path/to/database.sqlite'
});

// Option 2: Passing parameters separately (other dialects)
const sequelize = new Sequelize('database', 'username', 'password', {
  host: 'localhost',
  dialect: /* one of 'mysql' | 'mariadb' | 'postgres' | 'mssql' */
});
```

Optamos pela última opção, e o trecho de código ficou assim:
> 
```javascript
const { Sequelize } = require('sequelize');

const dialeto = 'mysql';
const host = 'localhost';
const database = 'db_chama_ti';
const username = 'root';
const password = 'bcd127';

// timestamp - Coloca created_at e updated_at nas tabelas
// underscored - Coloca os nomes de tabelas e atributos em snake_case

module.exports = {
  dialect : dialeto,
  host : host,
  username : username,
  password : password,
  database : database,
  logging: console.log,
  define : {
      timestamp : true,
      underscored : true
  }
}
```
Logo já podemos criar o banco de dados, conforme as configurações, com o comando:
>
```
npx sequelize db:create
```

### Migrations
Primeiro criamos um projeto vazio com o comando:
>
```
    npx sequelize-cli init
```
Obs: Este comando deve ser executado dentro do diretório onde estas pastas vão ficar (ex: src)

Este comando cria as sequintes pastas:
- config, contêm um arquivo config que fala para o CLI como conectar com o banco de dados
- models, contêm todos os modelos do projeto (que serão criados posteriormente)
- migrations, contêm todos os arquivos de migrations
- seeders, contêm todos os arquivos seed

### Configuração
Antes prossseguir é necessário informar ao CLI como conectar ao banco de dados. Para tal editamos o arquivo config/config.json.
Lá substituímos os valores com as informações do nosso banco de dados. Ficou assim:
> 
```json
{
  "development": {
    "username": "root",
    "password": "bcd127",
    "database": "chama_ti",
    "host": "127.0.0.1",
    "dialect": "mysql"
  },
  "test": {
    "username": "root",
    "password": "bcd127",
    "database": "chama_ti",
    "host": "127.0.0.1",
    "dialect": "mysql"
  },
  "production": {
    "username": "root",
    "password": "bcd127",
    "database": "chama_ti",
    "host": "127.0.0.1",
    "dialect": "mysql"
  }
}
```

### Criando modelo (e migrations)
Para criar um novo modelo por meio de migrations é necessário executar o seguinte comando:
>
```
npx sequelize migration:create --name nomeAqui
```

Logo depois o editamos a fim de modelar, efetivamente, a tabela, como neste exemplo:
>
```javascript
'use strict';

const { query } = require("express");

module.exports = {
  up: async (queryInterface, Sequelize) => {
    return queryInterface.createTable("tbl_cliente", {
      id: {
        type: Sequelize.INTEGER,
        primaryKey: true,
        autoIncrement: true
      },
      nome:  {
        type: Sequelize.STRING,
        allowNull: false
      },
      email:  {
        type: Sequelize.STRING,
        allowNull: false,
        unique: true
      },
      senha:  {
        type: Sequelize.STRING,
        allowNull: false
      },
      data_nascimento: {
        type: Sequelize.DATEONLY,
        allowNull: false
      },
      rg: {
        type: Sequelize.STRING,
        allowNull: false,
        unique: true
      },
      cpf: {
        type: Sequelize.STRING,
        allowNull: false,
        unique: true
      },
      telefone: {
        type: Sequelize.STRING,
        allowNull: false,
        unique: true
      },
      foto: {
        type: Sequelize.STRING,
        allowNull: true
      },
      sexo_cliente_id : {
        type: Sequelize.INTEGER,
        allowNull: false,
        references: {
          model: "tbl_sexo_cliente",
          key: "id"
        },
        onUpdate: "CASCADE",
        onDelete: "CASCADE"
      },
      created_at: {
        type: Sequelize.DATE,
        allowNull: false
      },
      updated_at: {
        type: Sequelize.DATE,
        allowNull: false
      }
    });
  },

  down: async (queryInterface, Sequelize) => {
    return queryInterface.dropTable("tbl_cliente");
  }
};
```

E para, efetivamente, criar o banco de dados executamos o comando:
>
```
npx sequelize db:migrate
```

### Criando as controllers das tabelas para manipulação pelo backend
Antes de criarmos uma controller precisamos criar sua respectiva model.
Criamos uma model e uma controller para cada tabela do BD, como no exemplo:

Model:
>
```javascript
const { Model, DataTypes } = require("sequelize");

class Cliente extends Model {
    static init(sequelize) {
        super.init(
            {
                id: {
                    type: DataTypes.INTEGER,
                    primaryKey: true
                },
                nome: DataTypes.STRING,
                email: DataTypes.STRING,
                senha: DataTypes.STRING,
                data_nascimento: DataTypes.DATEONLY,
                rg: DataTypes.STRING,
                cpf: DataTypes.STRING,
                telefone: DataTypes.STRING,
                foto: DataTypes.STRING,
                created_at: DataTypes.DATE,
                updated_at: DataTypes.DATE,
            },
            {
                sequelize,
                tableName: "tbl_cliente"
            }
        );
    }

    static associate(models) {
        this.belongsTo(models.SexoCliente, {
            foreignKey: "sexo_cliente_id"
        });
        this.hasOne(models.LocalizacaoCliente);
        this.hasOne(models.EnderecoCliente);
        this.hasMany(models.Servico);
        this.hasMany(models.Mensagem);
    }
}

module.exports = Cliente;
```

Após criar as models é necessário configurar o arquivo "index.js" dentro da pasta database(no caso de definir manualmente):
>
```javascript
const Sequelize = require("sequelize");
const dbConfig = require("../config/database");

const Cliente = require("../models/Cliente");
const EnderecoCliente = require("../models/EnderecoCliente");
const EnderecoPrestadorServicos = require("../models/EnderecoPrestadorServicos");
const ImagemServico = require("../models/ImagemServico");
const LocalizacaoCliente = require("../models/LocalizacaoCliente");
const LocalizacaoPrestadorServicos = require("../models/LocalizacaoPrestadorServicos");
const Mensagem = require("../models/Mensagem");
const PrestadorServicos = require("../models/PrestadorServicos");
const Servico = require("../models/Servico");
const SexoCliente = require("../models/SexoCliente");
const SexoPrestadorServicos = require("../models/SexoPrestadorServicos");

// Criamo a conexão com os dados da configuração
const conexao = new Sequelize(dbConfig);

// Inicializando as models
Cliente.init(conexao);
EnderecoCliente.init(conexao);
EnderecoPrestadorServicos.init(conexao);
ImagemServico.init(conexao);
LocalizacaoCliente.init(conexao);
LocalizacaoPrestadorServicos.init(conexao);
Mensagem.init(conexao);
PrestadorServicos.init(conexao);
Servico.init(conexao);
SexoCliente.init(conexao);
SexoPrestadorServicos.init(conexao);

// Inicializando as associações
Cliente.associate( conexao.models );
EnderecoCliente.associate( conexao.models );
EnderecoPrestadorServicos.associate( conexao.models );
ImagemServico.associate( conexao.models );
LocalizacaoCliente.associate( conexao.models );
LocalizacaoPrestadorServicos.associate( conexao.models );
Mensagem.associate( conexao.models );
PrestadorServicos.associate( conexao.models );
Servico.associate( conexao.models );
SexoCliente.associate( conexao.models );
SexoPrestadorServicos.associate( conexao.models );

// Exportamos a conexão
module.exports = conexao;
```

Controller:
>
```javascript
const bcrypt = require("bcryptjs");
const Cliente = require("../models/Cliente");

module.exports = {
    // Listar todos os clientes
    async list( request, response ) {
        const clientes = await Cliente.findAll();

        return response.send( clientes );
    },

    // Buscar clientes pelo ID
    async searchById( request, response ){
        const { id } = request.params;

        let cliente = await Cliente.findByPk( id, { raw : true } );

        // Verifica se o cliente não foi encontrado
        if( !cliente ){
            return response.status( 404 ).send( { erro : "Cliente não encontrado." } )
        }

        // Apaga o campo senha da resposta para não mostrá-la a quem solicitou a busca
        delete cliente.senha;

        // Retorna o cliente encontrado
        return response.send( cliente );
    },

    // Inserções
    async store(request, response){
        const {
            sexo_id,

            cep,
            logradouro,
            bairro,
            cidade,
            estado,
            numero,
            complemento,

            nome,
            email,
            senha,
            data_nascimento,
            cpf,
            telefone,
            foto
        } = request.body;

        // Verificar se o cliente já existe
        //      select * from clientes where rg = ? or email = ? or cpf = ?
        let cliente = await Cliente.findOne(
            {
                 where: {
                    email : email
                 }
            }
        );

        if ( cliente ) { 
            return response.status( 400 ).send( { erro : "Cliente já cadastrado." } )
        }

        const senhaCripto = await bcrypt.hash(senha, 10);

        if( foto ){
            cliente = await Cliente.create({
                nome, email, senha: senhaCripto, data_nascimento, cpf, telefone, foto, sexo_cliente_id : sexo_id
            });
        }
        else {
            cliente = await Cliente.create({
                nome, email, senha: senhaCripto, data_nascimento, cpf, telefone, sexo_cliente_id : sexo_id
            });
        }

        let endereco_cliente;

        if(cliente){
            endereco_cliente = await cliente.createEnderecoCliente({
                cep,
                logradouro,
                bairro,
                cidade,
                estado,
                numero,
                complemento,
            });
        }
        else {
            return response.status( 400 ).send( { erro : "Erro ao cadastrar o cliente. Tente novamente." } )
        }

        if( !endereco_cliente ){
            return response.status( 400 ).send( { erro : "Erro ao cadastrar o endereco. Tente novamente." } )
        }

        return response.status(201).send({
            cliente: {
                cliente_id: cliente.id_cliente,
                nome: cliente.nome,
                cpf: cliente.cpf,
                endereco: {
                    logradouro : endereco_cliente.logradouro,
                    bairro : endereco_cliente.bairro,
                    cidade : endereco_cliente.cidade,
                    estado : endereco_cliente.estado,
                    numero : endereco_cliente.numero,
                    complemento : endereco_cliente.complemento,
                }
            },
            // token
        });
    },

    //Terminar de implementar
    async update( request, response ){
        const { id } = request.params;

        let cliente = await Cliente.findByPk( id, { raw : true } );

        // Verifica se o cliente não foi encontrado
        if( !cliente ){
            return response.status( 404 ).send( { erro : "Cliente não encontrado." } )
        }

        const {
            sexo_id,

            cep,
            logradouro,
            bairro,
            cidade,
            estado,
            numero,
            complemento,

            nome,
            email,
            senha,
            data_nascimento,
            cpf,
            telefone,
            foto
        } = request.body;

        const senhaCripto = await bcrypt.hash(senha, 10);

        let cliente_update;

        if( foto ){
            cliente_update = cliente.update({
                nome, email, senha: senhaCripto, data_nascimento, cpf, telefone, foto, sexo_cliente_id : sexo_id
            });
        }
        else {
            cliente_update = cliente.update.update({
                nome, email, senha: senhaCripto, data_nascimento, cpf, telefone, sexo_cliente_id : sexo_id
            });
        }

        // Apaga o campo senha da resposta para não mostrá-la a quem solicitou a busca
        delete cliente.senha;

        let endereco_cliente_update;

        if(cliente_update){
            endereco_cliente_update = await cliente.updateEnderecoCliente({
                cep,
                logradouro,
                bairro,
                cidade,
                estado,
                numero,
                complemento,
            });
        }
        else{
            return response.status( 404 ).send( { erro : "Atualização mal sucedida, tente novamente." } )
        }

        if(endereco_cliente_update){
            return response.status(201).send({
                cliente_update, endereco_cliente_update
                // token
            });
        }
    },

    //Terminar de implementar
    async delete( request, response ){
        const { id } = request.params;

        let cliente = await Cliente.findByPk( id, { raw : true } );

        // Verifica se o cliente não foi encontrado
        if( !cliente ){
            return response.status( 404 ).send( { erro : "Cliente não encontrado." } )
        }

        let deleta = cliente.destroy;

        if(deleta){
            return response.status( 404 ).send( { erro : "Cliente excluído com sucesso." } )
        }
        else {
            return response.status( 404 ).send( { erro : "Falha na exclusão do cliente." } )
        }
    }
}
```

E para efetivamente usar estas rotas é necessário cadastrá-las no arquivo "routes.js" (trecho do arquivo routes com funções de outras entidades faltando):
>
```javascript
// Esse arquivo tem como responsabilidade cadastrar as rotas da aplicação

const express = require("express");

// const multer = require("multer");

// const Multer = multer({
//     storage: multer.memoryStorage(),
//     limits: 1024 * 1024,

// })

// Criando o roteirizador
const routes = express.Router();

const autorizacaoMid = require("./middlewares/autorizacao");
// const uploadImage = require("./services/firebase");

const clienteController = require("./controller/cliente");
const sessaoController = require("./controller/sessao");
const sexoClienteController = require("./controller/sexo_cliente");

// Rotas públicas

// Rota de cadastro de cliente
routes.post("/cliente", clienteController.store);

// Rota de cadastro de sexo_cliente
routes.post("/sexo_cliente", sexoClienteController.store);

// Rotas de autenticação sessão
routes.post("/sessao/cliente", sessaoController.clienteAuthenticate);

// Middleware de proteção das rotas
routes.use(autorizacaoMid);

// Rotas privadas

// Rotas de cliente
routes.get("/clientes", clienteController.list);
routes.get("/cliente/:id", clienteController.searchById);

// Rotas de sexo_cliente
routes.get("/sexos_clientes", sexoClienteController.list);
routes.get("/sexo_cliente/:id", sexoClienteController.searchById);
routes.post("/sexo_cliente/update/:id", sexoClienteController.update);
routes.post("/sexo_cliente/delete/:id", sexoClienteController.delete);

module.exports = routes;
```

No código acima há, também, rotas de sessão que foram desenvolvidas num outro arquivo que utiliza das ferramentas "jwt" e "bcrypt" que, respectivamente, faz o "login" e gera um token e encripta e pode ser usado para comparar uma string com a string que foi encriptada por ele:
>
```javascript
const Cliente = require("../models/Cliente");
const PrestadorServicos = require("../models/PrestadorServicos");

const bcrypt = require("bcryptjs");
const jwt = require("jsonwebtoken");
const authConfig = require('../config/auth.json');

module.exports = {
    async clienteAuthenticate ( request, response ) {
        const { email, senha } = request.body;

        // Busca um cliente com o email informado
        const cliente = await Cliente.findOne({
            where: {
                email,
            }
        });

        // Verifica se o cliente existe e a senha corresponde a senha informada
        if( !cliente || !( await bcrypt.compare( senha, cliente.senha ) ) ){
            return response.status(403).send({erro : "Email e/ou senha incorretos."});
        }

        // Gera um token que valida a autenticação do cliente
        const token = jwt.sign({ user_id: cliente.id, user_name: cliente.nome, user_access: "cliente" }, authConfig.secret);

        return response.status(201).send({
            cliente: {
                id: cliente.id,
                nome: cliente.nome,
            },
            token
        });
    },

    async prestadorServicoAuthenticate ( request, response ) {
        const { email, senha } = request.body;

        // Busca um cliente com o email informado
        const prestador_servicos = await PrestadorServicos.findOne({
            where: {
                email,
            }
        });

        // Verifica se o prestador serviço existe e a senha corresponde a senha informada
        if( !prestador_servicos || !( await bcrypt.compare( senha, prestador_servicos.senha ) ) ){
            return response.status(403).send({erro : "Email e/ou senha incorretos."});
        }

        // Gera um token que valida a autenticação do prestador serviço
        const token = jwt.sign({ user_id: prestador_servicos.id, user_name: prestador_servicos.nome, user_access: "prestador_servicos" }, authConfig.secret);

        return response.status(201).send({
            prestador_servicos: {
                id: prestador_servicos.id,
                nome: prestador_servicos.nome,
            },
            token
        });
    },

    // Implementar um autenticador genérico
    async userAutenticate () {

    }
}
```

E este arquivo, por sua vez, necessita de um outro, o "auth.json" que apenas contém a palavra chave encriptografada:

>
```json
{
    "secret": "4b3c0d65bd58c188a12bdf0664803ba6"
}
```