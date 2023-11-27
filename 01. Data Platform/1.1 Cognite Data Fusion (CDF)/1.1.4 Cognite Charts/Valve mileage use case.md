# Valve mileage use case

The valve stem controls gas flow in the first stage of gas treatment system. To prevent the compressor from surging, the steam needs to move up and down at a rapid pace. Every second, the steam rubs against the packing, leaving it vulnerable to abrasion. In the case of compressor malfunction, production will come to a halt, creating a world of trouble for operators.

!["Valve mileage 01"](img/valve%20mileage%20use%20case-01.png)
!["Valve mileage 02"](img/valve%20mileage%20use%20case-02.png)


Typically, valve maintenance is conducted according to a fixed schedule based on parameters like total running time. This process is inefficient because over a given period, you could end up maintaining a valve that is already overdue or one that does not yet require maintenance.

Thankfully, the valve has sensors that feed data points to a control system each time it changes position. Instead of relying on running time, the engineer responsible for it could calculate the distance it has traveled. Calculating the valve mileage can provide valuable input by determining the distance the valve has moved over a given timespan, which is crucial for conducting smart, condition-based maintenance.

## Mathematical explanation

To calculate the total of valve mileage, we aim to understand the process of deriving total distance covered based on the valve's position over time. First, we seek to convert propostional opening from zero to 100  into a metric value, specifically in centimeters. To achieve this, we divede the valve's opening percentile by one hundred, normalizing the percentage to a range between 0 and 1. Subsequently, we mutiply this value by the actual maximum valve travel length, which is 40 centimeters. 

Now, for the dynamics, we can analyze the valve's movement. The initial step involves taking the derivative of the position concerning time. This allows us to transition from a position to a precision change, representing the velocity of the valve in units of centimeters per second. By doing so, we determine the time rate of change in the valve's position. Next, we obtain the absolute value of the velocity to transform it into speed, eliminating direction since it's irrelevant to our goal - we're interested in movements, regardless of the valve's opening or closing direction.

Finally, we accumulate our movement by integrating concerning time. As we differentiate per second, integration should also occur per second, thus eliminating the time dimension and providing us with the distance the valve has traveled.






































A haste da válvula controla o fluxo de gás na primeira etapa do sistema de tratamento de gás. Para evitar que o compressor oscile, a haste precisa mover-se para cima e para baixo no ritmo rápido. A cada segundo, a haste atrita contra o revestimento, deixando-a vulnerável à abrasão. Em caso de mau funcionamento do compressor, a produção será interrompida, criando um mundo de problemas para os operadores.

Tipicamente, a manutenção de válvulas é realizada de acordo com um cronograma fixo baseado em parâmetros como tempo total de funcionamento. Esse processo é ineficiente porque, ao longo de um período determinado, você pode acabar realizando a manutenção de uma válvula que já está atrasada ou de uma que ainda não requer manutenção.

Para calcular o total de quilometragem da válvula, buscamos entender o processo de obtenção da distância total percorrida com base na posição da válvula ao longo do tempo. Primeiramente, procuramos converter a abertura proporcional de zero a 100 para um valor métrico, especificamente em centímetros. Para alcançar isso, dividimos o percentual de abertura da válvula por cem, normalizando a porcentagem para uma faixa entre 0 e 1. Em seguida, multiplicamos esse valor pelo comprimento máximo real de deslocamento da válvula, que é de 40 centímetros.

Agora, em relação à dinâmica, podemos analisar o movimento da válvula. O primeiro passo envolve a obtenção da derivada da posição em relação ao tempo. Isso nos permite transitar de uma posição para uma mudança de precisão, representando a velocidade da válvula em centímetros por segundo. Ao fazer isso, determinamos a taxa de mudança no tempo da posição da válvula. Em seguida, obtemos o valor absoluto da velocidade para transformá-la em velocidade, eliminando a direção, pois não é relevante para nosso objetivo - estamos interessados nos movimentos, independentemente da direção de abertura ou fechamento da válvula.
