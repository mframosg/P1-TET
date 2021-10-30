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

![Arquitectura](https://i.imgur.com/CKPCMGt.png)

### Cliente

El cliente se comunica con el servidor a través de solicitudes tipo **GET** y  **POST**, teniendo cada una de estas un propósito diferente.

#### GET

Se usa en el cliente para obtener información de la existencia de un determinado registro en nuestra base de datos. Se le pasa un **ID** de registro y se consulta a los nodos si hay alguna información relacionada con el número de cédula suministrado.

#### POST

En el cliente hacemos uso de solicitudes POST en la operación de agregar, lo usamos para enviar los datos recolectados de cada registro a archivos **JSON**, que almacenarán los datos de manera distribuida. Todos los archivos **JSON** contienen la clave de la cédula, pero cada uno por su parte almacena un atributo diferente de cada registro.

##### Ejemplo de registro

Vamos a tener un registro de la forma:

    {
        "id": "12345678",
        "name": "Juan",
        "age": "18",
        "city": "Cartagena",
        "score": "400"
    }

Este registro se almacenará de tal forma que en el nodo de **Nombres** se vea así:

    {
        "id"; "12345678",
        "name": "Juan"
    }

En el nodo de **Edades** encontraremos el registro así:

    {
        "id"; "12345678",
        "age": "18"
    }

En el nodo de **Ciudades** encontraremos el registro así:

    {
        "id"; "12345678",
        "age": "Cartagena"
    }

En el nodo de **Puntajes** encontraremos el registro así:

    {
        "id"; "12345678",
        "score": "400"
    }

## Load Balancer

Este se encarga de distribuir el tráfico entre dos o más servidores, esto se hace con propósitos de escalabilidad.

Podemos agregar tantos servidores como queramos. Todos los servidores tienen el mismo funcionamiento. Estos reciben una consulta, y si esta es de tipo **POST**, procede a hacer consultas tipo **POST** a los nodos.

### Nodos

Los nodos nos sirven para almacenar datos de manera distribuida, teniendo un nodo para cada atributo del registro. Es decir: tenemos un nodo para los **nombres**, otro para las **edades**, otro para las **ciuades**, otro para los **puntajes**. Recordemos que en cada nodo, el **ID** (cédula) se encuentra relacionado con el valor del atributo correspondiente al nodo en cuestión.

### Servidor

El servidor se encarga de comunicarse con los nodos y de asignarle una key a cada fragmento de datos que recibe. Antes de realizar el particionamiento, se asignará a cada fragmento una key que corresponde a la cédula del registro en cuestión, para identificar los diferentes fragmentos que conforman ese registro completo. Como las cédulas son únicas e irrepetibles, las usamos como keys. Es como cuando en una base de datos MySQL usamos una primary key que no se vaya a repetir. Posteriormente, se realiza el particionamiento de la forma **<cédula, nombre>**, **<cédula, edad>**, **<cédula, ciudad>**, etc. Cada fragmento de datos se envía a su nodo correspondiente con una solicitud de tipo **POST**.

El nodo recibe el **JSON** y posteriormente almacena la información.

### Consultas

Para realizar la búsqueda de un registro a partir de un número de cédula suministrado por el usuario, se van haciendo consultas **GET** a los nodos para ver si esta clave se encuentra en nuestra base de datos. Si efectivamente existe, el servidor consulta a los nodos para recopilar cada fragmento del registro en cuestión. Esta información se guarda en un **JSON** que está en el servidor, donde en cada registro se almacena la información recuperada. En caso de no encontrarse el registro que se busca, se responderá con un **error 404 (not found)**.
