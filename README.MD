### PATRONES ARQUITECTONICOS

**Singleton**

Es un patron que pertence a la categoria de creativos, dentro del grupo de patrones de diseño. El objetivo de este patron es que se evite crear mas de un objeto por clase. Esto se consigue creando el objeto en una clase y recuperandolo como una instancia estatica. <br> Asi nos permite tener una unica instancia de una clase lo que nos provee mas rendimiento.

**Factory**

Es un tipo de diseño que nos permite crear un objeto sin especificar su clase exacta. Lo que ayuda a que un objeto creado pueda intercambiarse con flexibilidad y facilidad.<br> Se puede implementar usando una interfaz o usando la clase hijo o la clase base y opcionalmente sobreescribirse. El patron toma el lugar del constructor de clase para separar la creacion de objetos de los propios objetos. Este nos provee flexibilidad al no depender de una instancia.

**Abstract factory**

Este patron, tienne relacion con el factory, en este caso tendriamos una factory aun mas grande que contiene diferentes fabricas. Mediante esta factory mas grande podemos acceder a una de las que contiene y necesitamos, estas se agrupan por familias que tienen cosas en comun. Todo esto nos permite agrupar las factory de acuerdo a ciertas caracteristicas en comun para mantener una gran consistencia.

**Prototype**

Es un tipo de patron que basa su funcionamiento en la clonacion de objetos, los nuevos objetos son creados con un pool que contiene varios prototipos elaborados anteriormente y alamcenados. Es generalmente util cuando se necesita crear objetos apartir de otros que ya existen o para hacer la estructura de otros muy grandes.

**Facade**

Es una patron que se encarga de ocultar lo complejo que es interactuar con un conjunto de subsistemas proporcionando una interfaz, la cual realiza las comunicaciones necesarias. Es un patron que destaca por su usa cuando necesitamos interactuar con varios subsistemas para realizar una operacion en concreto.

**Decorator**

Es un patron que tiene la funcion de solucionar los problemas que surgen donde la jerarquia con subclasificacion no puede ser aplicada, o se necesita que haya un gran impacto en las jerarquias para lograr lo esperado. Se logra por medio de una clase decorador que tendra que recibir un constructor y lo va a pasar a otra clase sin afectar el funcionamiento de esta. Este permite añadir nuevas funcionalidades a un objeto sin la necesidad de alterar su estructura.

**Proxy**

Es una patron que se enfoca en la mediacion entre un objeto y otro, nos permite crear un envoltorio que nos provee la opcion de hacer de intermediario entre el cliente y el objeto real, actua como una clase intermediaria que delega roles o informacion. Se puede usar para añadir funcionalidades sin tener que acceder a las clase final.

**Command**

Es un patron que permita que se ejecuten operaciones sin conocer los detalles de la implementacion, estas operaciones son conocidas como comandos, cada operacion se implementa como una clase que realiza una accion en concreto. Este patron nos permite crear comandos y encapsularlos en una interfaz de ejecucion.

**Memento**

Es un patron que permite capturar el estado de un objeto con el objetivo de retornar este estado en cualquier momento, se usa mas que todo cuando un objeto cambia en el tiempo y en algun momento necestamos que vuelva a un estado anterior.

**Observer**

Es un patron que define la dependencia entre barios objetos para transmitir los cambios de un objeto en concreto de una forma sencilla. Para esto se establece que un objeto es observado por otro, el que observa informa cada vez que el otro es modificado.

**Strategy**

Es un patron que permite establecer un grupo de algoritmos, que son independientes de los clientes. Este se basa en un polimorfismo que permite implementar algorimos que podran ser intercambiados.

**DAO**

El DAO es un patron que nos permite separar la logica del acceso de atos de los objetos, esto encapsula la logica al resto de la aplicacion. Esto se da al momento que tenemos que usar mas de una fuente de datos.

**Dependency Injection**

Es un patron que nos provee el objeto que solicitamos sin saber informacion como sus connstructores o como se hizo. Esto se hace mediante un metodo constructor que recibe objetos y retorna lo que al final solicitamos.

**MVC**

Es un patron que permite organizar los componentes de presentacion en sistemas distribuidos. Esta nos provee las posibilidad de separar los componentes de una aplicacion en tres capas modelo, vista y controlador.