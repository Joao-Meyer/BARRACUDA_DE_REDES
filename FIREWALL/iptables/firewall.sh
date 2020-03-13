#!/bin/bash

### BEGIN INIT INFO
# Provides:		firewall
# Required-Start:	$syslog
# Required-Stop:	$syslog
# Default-Start:	2 3 4 5
# Default-Stop:		0 1 6
# Short-Description:	Firewall
### END INIT INFO

case $1 in

start)
	
	echo 1 > /proc/sys/net/ipv4/ip_forward
	iptables -t nat -A POSTROUTING -o enp0s8 -j MASQUERADE
;;
stop)
	echo 0 > /proc/sys/net/ipv4/ip_forward
	iptables -t filter -F
	iptables -t mangle -F
	iptables -t nat -F
	iptables -t raw -F
	iptables -t security -F
;;
restart)
	$0 stop
	$0 start
;;
*)
	echo "Por favor use (stop | start | restart)"
;;

esac
