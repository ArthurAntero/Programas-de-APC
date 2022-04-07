x = input().split();
Horarios = [0,0,0,0,0,0, #M1
            0,0,0,0,0,0, #M2
            0,0,0,0,0,0, #M3
            0,0,0,0,0,0, #M4
            0,0,0,0,0,0, #M5
            0,0,0,0,0,0, #T1
            0,0,0,0,0,0, #T2
            0,0,0,0,0,0, #T3
            0,0,0,0,0,0, #T4
            0,0,0,0,0,0, #T5
            0,0,0,0,0,0, #T6
            0,0,0,0,0,0, #N1
            0,0,0,0,0,0, #N2
            0,0,0,0,0,0, #N3
            0,0,0,0,0,0] #N4
def add():
    if "M" in x[2]:
        semana,hora = x[2].split("M");
        tamSemana = len(semana);
        tamHora = len(hora);
        while tamSemana > 0:
            while tamHora > 0:
                Horarios[((int(semana[tamSemana-1])-1) + 6*(int(hora[tamHora-1])-1))-1] = x[1];
                tamHora -= 1;
            tamHora = len(hora);
            tamSemana -= 1;
    elif "T" in x[2]:
        semana,hora = x[2].split("T");
        tamSemana = len(semana);
        tamHora = len(hora);
        while tamSemana > 0:
            while tamHora > 0:
                Horarios[30+((int(semana[tamSemana-1])-1) + 6*(int(hora[tamHora-1])-1))-1] = x[1];
                tamHora -= 1;
            tamHora = len(hora);
            tamSemana -= 1;
    elif "N" in x[2]:
        semana,hora = x[2].split("N");
        tamSemana = len(semana);
        tamHora = len(hora);
        while tamSemana > 0:
            while tamHora > 0:
                Horarios[66+((int(semana[tamSemana-1])-1) + 6*(int(hora[tamHora-1])-1))-1] = x[1];
                tamHora -= 1;
            tamHora = len(hora);
            tamSemana -= 1;
def delete():
    return

while x[0] != "Hasta":
    if x[0] == "?":
        print(Horarios);
    elif x[0] == "+":
        add();
    elif x[0] == "-":
        delete();
    x = input().split();