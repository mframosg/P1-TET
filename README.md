# Proyecto #1 - Tópicos Especiales en Telemática - 2021-2 - Universidad EAFIT - Sistema de Almacenamiento de Datos Distribuido

## Conceptos fundamentales

Tenemos un conjunto de NODOS, los cuales almacenarán registros de una aplicación cliente en el formato <k,v> (key, value). El objetivo es diseñar e implementar un sistema ‘minimalista’ que permita almacenar datos distribuidos en los NODOSpor parte de los clientes. Por ‘minimalista’ quiere decir que usará una visión desde la más simple, pero deberá dejar explicito los retos reales que  enfrentan  sistemas  similares  ‘robustos’,  escalables,  confiables,  consistentes.Realice  todos los supuestos y restricciones que considere, siendo consciente de ella.

A continuación se enumeran los retos principales del sistema:

* Almacenamiento distribuido de datos - Recuperación Distribuida o Centralizada.
* Replicación
* Particionamiento
* Toleracia a fallos
* Escalabilidad
* WORM vs WMRM
* Cliente/Servidor vs P2P vs híbrido C/S-P2P, con todas las variantes posibles de C/S y P2P.
* Transacciones, Bloque u Objetos.

Requerimientos:

* La visión global del sistema es un cliente externo interesado en Almacenar datos <k, v> en un sistema distribuido .
    * El sistema permitirá almacenar **n** registros con la misma clave \<k>
* La recuperación de los datos se realizará por \<k>
    * Escenarios para k retornando un solo valor, k retornando algunos datos, k retornando muchos datos, k retornando gran cantidad de datos.
* Puede ser diseñado como una base de datos distribuida <k, v> o como un sistema de archivos distribuido o como un sistema de mensajería distribuido.
* Lo puede implementar sobre protocolos TCP/UDP con sockets o con protocolos HTTP.

Fundamentación:

* Arquitecturas C/S y P2P
* Fundamentos en Sistemas Distribuidos
* Fundamentos en Bases de datos distribuidas
* Fundamentos en Sistemas de Mensajería Distribuida
  * Teorema CAP
  * Replicación, Particionamiento, Transacciones, Consistencia, Consenso.
* Fundamentos en Sistemas de Archivos Distribuidos.

### Fecha de entrega

* 3 de octubre de 2021

## Integrantes

* Alejandro Fernández Restrepo
* Miguel Fernando Ramos García
* Simón Marín Giraldo

## Solución

La solución planteada para este problema se puede ver representada en la siguiente arquitectura:

imagen

### Cliente

El cliente se comunica con el servidor a través de solicitudes tipo **GET** y  **POST**, teniendo cada una de estas un propósito diferente.

#### GET

Se usa en el cliente para obtener información de la existencia de un determinado registro en nuestra base de datos. Se le pasa un **ID** de registro y se busca si este existe.

#### POST

En el cliente hacemos uso de solicitudes POST en la operación de agregar, lo usamos para enviar los datos recolectados de cada registro a archivos **JSON**, que almacenarán los datos de manera distribuida. Todos los archivos **JSON** contienen la clave de la cédula, pero cada uno por su parte almacena un atributo diferente de cada registro.

##### Ejemplo de registro

Vamos a tener un registro de la forma:

    {
        "id": "12345678",
        "name": "Juan",
        "city": "Cartagena",
        "score": "400"
    }

## Load Balancer

Este se encarga de distribuir el tráfico entre dos o más servidores, esto se hace con propósitos de escalabilidad.

Podemos agregar tantos servidores como queramos. Todos los servidores tienen el mismo funcionamiento. Estos reciben una consulta, y si esta es de tipo **POST**, procede a hacer consultas tipo **POST** a los nodos. Est

## Nodos

Los nodos nos sirven para almacenar datos de manera distribuida, teniendo un nodo para cada atributo del registro. Es decir: tenemos un nodo para los **nombres**, otro para las **ciuades**, otro para los **puntajes**. Recordemos que en cada nodo, el **ID** (cédula) se encuentra relacionado con el valor del atributo correspondiente al nodo en cuestión.
