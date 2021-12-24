<p align="center">
    <img src="https://github.com/GeeksHubsAcademy/2020-geekshubs-media/blob/master/image/logo.png" >	
</p>


    Considere el siguiente problema:

    Escriba un programa corto donde se tenga un array de enteros como parámetro de entrada y otro como resultado de salida.
    Se necesita calcular las siguientes operaciones.

    Clasifica :
    Números positivos.
    Números negativos.
    Números igual a 0.
         
    Calcula el número de elementos de cada clasificación, dividido por el número del array.
    Represente el número de cada operación con un redondeo de 4 decimales.
    Devuelva un array de salida con cada operación en el siguiente orden [Npositivos, Nnegativos, Nzero]
     
    Se atiente al siguiente ejemplo:
   
    Array: [1, 2 ,-8, -2, 0, 9]
    
    Números positivos = 1, 2, 9
    Números negativos = -8, -2
    Números igual a 0 = 0
   
    Resultado: [(Npositivios/Array.size), (Nnegativos/Array.size), (Nzero/Array.size)]
    

    En la carpeta 'tests/test_kata.py' se encuentra el fichero con la definición de nuestro método vacío.
    
    El modus operandi de trabajo es el siguiente:
    
    Debes 'forkear' el proyecto a tu cuenta.
    Puedes hacer PR's ilimitadas e ir validando poco a poco la solución contra nuestro respositorio con CI.
    Puedes trabajar en local y subir la solución haciendo un PR a nuestro repositorio.
    Cuando se envíe la PR final, debes indicar el tiempo de dedicación y los intentos que has hecho.
    También puedes añadir un comentario para dar cualquier tipo de feedback.
    
    En caso de duda, revisa en el apartado de 'Referencias'.       
    

   [Suite Tests]
    
    def test_apply_with_Array_0(self):
        asserted = ["0.0000", "0.0000", "1.0000"] 
        result = apply([0])
        assert(result == asserted)
   

    def test_apply_with_Array_1(self):
        asserted = ["0.0000", "1.0000", "0.0000"] 
        result = apply([-4])
        assert(result == asserted)
   

    def test_apply_with_Array_2(self):
        asserted = ["1.0000", "0.0000", "0.0000"] 
        result = apply([10])
        assert(result == asserted)
   

    def test_apply_with_Array_3(self):
        asserted = ["0.5000", "0.3333", "0.1667"] 
        result = apply([-4, 3, -9, 0, 4, 1])
        assert(result == asserted)
   

    def test_apply_with_Array_4(self):
        asserted = ["0.5000","0.3333", "0.1667"] 
        result = apply([5, -2, -9, 2, 0, 9])
        assert(result == asserted)
   

    def test_apply_with_Array_5(self):
        asserted = ["0.1667","0.1667", "0.6667"] 
        result = apply([0, 0, 0, 10, 0, -8])
        assert(result == asserted)
   

    def test_apply_with_Array_6(self):
        asserted = ["0.0000", "0.6667", "0.3333"] 
        result = apply([-5, -6, -9, -6, 0, 0])
        assert(result == asserted)
   

    def test_apply_with_Array_7(self):
        asserted = ["0.5000","0.5000", "0.0000"] 
        result = apply([5, 2, 9, -2, -2, -9])
        assert(result == asserted)
   

    def test_apply_with_Array_7(self):
        asserted = ["0.3333", "0.3333","0.3333"] 
        result = apply([10, 0, -8])
        assert(result == asserted)


    /**
     PASS  ./suite.test.js
     v clasificaElementos with Array [0] (3ms)
     v clasificaElementos with Array [-1] (1ms)
     v clasificaElementos with Array [6]
     v clasificaElementos with Array [-4, 3, -9, 0, 4, 1] (6ms)
     v clasificaElementos with Array [5, -2, -9, 2, 0, 9]
     v clasificaElementos with Array [0, 0, 0, 10, 0, -8] (1ms)
     v clasificaElementos with Array [-5, -6, -9, -6, 0, 0] (1ms)
     v clasificaElementos with Array [5, 2, 9, -2, -2, -9]
     v clasificaElementos with Array [10, 0,-8] (1ms)

     Test Suites: 1 passed, 1 total
     Tests:       9 passed, 9 total
     Snapshots:   0 total
     Time:        3.829s
     Ran all test suites.
     **/


## Referencias

* [Tutorial - Testing Automatizado](https://github.com/GeeksHubsAcademy/2020-js-vanilla-testing-FFFF/blob/master/README.md)
