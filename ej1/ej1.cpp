#include <algorithm>
#include <iostream>
#include <limits.h>
#include <math.h>
#include <map>
#include <set>

using namespace std;

struct Punto {
  int x;
  int y;
  Punto() {};
  Punto(int x1, int y1) {
    x = x1;
    y = y1;
  };
  bool operator<(const Punto& p2) const {
    return (x < p2.x || (x == p2.x && y < p2.y));
  }
};

void definir(map<Punto, set<Punto>>& dic, Punto& p) { // Define el punto 'p' en el diccionario 'dic' si no esta definido
  if(dic.count(p) <= 0) {
    dic.insert(pair<Punto, set<Punto>>(p, set<Punto>()));
  }
}

void generarContorno(map<Punto, set<Punto>>& dic, Punto& p1, Punto& p2) {
  if(dic.find(p1)->second.count(p2) > 0) { // Si p1 esta conectado con p2, los desconecto ya que es un lado que comparte dos triangulos (el actual y uno anterior)
    dic.find(p1)->second.erase(p2);
    dic.find(p2)->second.erase(p1);
  } else { // Si no estan conectados, los conecto
    dic.find(p1)->second.insert(p2);
    dic.find(p2)->second.insert(p1);
  }
}

void mostrarPunto(Punto p) {
  cout << p.x << " " << p.y << " ";
}

double distancia(Punto p1, Punto p2) { // Calcula la distancia euclidea
  return sqrt(pow(p1.x-p2.x, 2) + pow(p1.y-p2.y, 2));
}

bool sentidoHorario(Punto pivot, Punto p1, Punto p2) { // Determina si desde p1 se va hacia p2 en sentido horario (o sea que luego del pivot, en sentido horario viene p1)
  bool res;
  
  // Calculo el area del paralelogramo, teniendo cuidado y llevando los vectores al (0,0) con respecto al pivot
  int area = ((p2.x-pivot.x)*(p1.y-pivot.y)) - ((p2.y-pivot.y)*(p1.x-pivot.x));
  if(area > 0) {
    res = true;
  } else if(area < 0) {
    res = false;
  } else { // Si estan en la misma recta, entonces p1 va a ir antes que p2 solo si tiene menor distancia hacia el pivot que p2
    res = (distancia(pivot, p1) < distancia(pivot, p2));
  }
  
  return res;
}

int main() {
  ios_base::sync_with_stdio(false);
  int N;
  cin >> N;
  
  Punto inicial(INT_MAX, INT_MAX);
  map<Punto, set<Punto>> conexiones;
  for(int i = 0; i < N-2; i++) {
    Punto p1, p2, p3;
    cin >> p1.x >> p1.y >> p2.x >> p2.y >> p3.x >> p3.y; // Obtengo los tres puntos del triangulo actual

    inicial = min(inicial, min(p1, min(p2, p3))); // Voy calculando el punto con el que tengo que iniciar el output
    
    definir(conexiones, p1);
    definir(conexiones, p2);
    definir(conexiones, p3);
    
    // Luego, los 3 puntos (p1, p2 y p3) existen en el diccionario
    
    generarContorno(conexiones, p1, p2);
    generarContorno(conexiones, p1, p3);
    generarContorno(conexiones, p2, p3);
  }
  
  mostrarPunto(inicial);
  
  Punto p1, p2;
  set<Punto>::iterator it = conexiones.find(inicial)->second.begin();
  p1 = *it; // Primer punto adyacente al punto inicial
  it++;
  p2 = *it; // Segundo punto adyacente al punto inicial
  
  // Ahora hay que ver cual de los dos puntos adyacentes al punto inicial le sigue en sentido horario para realizar el output
  
  if(sentidoHorario(inicial, p1, p2)) { // Si luego de inicial viene p1 recorriendo el plano en sentido horario...
    conexiones.find(inicial)->second.erase(p1);
    conexiones.find(p1)->second.erase(inicial);
    inicial = p1;
  } else { // Sino, entonces viene p2
    conexiones.find(inicial)->second.erase(p2);
    conexiones.find(p2)->second.erase(inicial);
    inicial = p2;
  }

  for(int i = 0; i < N-1; i++) { // Imprimo el resto de los puntos, teniendo cuidado y borrando los ejes que ya fui recorriendo
    cout << inicial.x << " " << inicial.y;
    if(i != N-2) cout << " ";
    Punto p1 = *(conexiones.find(inicial)->second.begin());
    conexiones.find(inicial)->second.erase(p1);
    conexiones.find(p1)->second.erase(inicial);
    inicial = p1;
  }
  
  cout << endl;
  
  return 0;
}