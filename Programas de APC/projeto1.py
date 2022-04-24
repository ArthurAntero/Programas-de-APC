x = input()
Hor = ["        "]*90
def add():
    i = 2;
    while i < len(x):
        if "M" in x[i]:
            semana,hora = x[i].split("M");
            tamSemana = len(semana);
            tamHora = len(hora);
            if Hor[((int(semana[tamSemana-1])-1) + 6*(int(hora[tamHora-1])-1))-1] != "        ":
                print(f"!(+ {x[1]} {x[i]})");
            else:
                while tamSemana > 0:
                    while tamHora > 0:
                        Hor[((int(semana[tamSemana-1])-1) + 6*(int(hora[tamHora-1])-1))-1] = x[1];
                        tamHora -= 1;
                    tamHora = len(hora);
                    tamSemana -= 1;
        elif "T" in x[i]:
            semana,hora = x[i].split("T");
            tamSemana = len(semana);
            tamHora = len(hora);
            if Hor[30+((int(semana[tamSemana-1])-1) + 6*(int(hora[tamHora-1])-1))-1] != "        ":
                print(f"!(+ {x[1]} {x[i]})");
            else:
                while tamSemana > 0:
                    while tamHora > 0:
                        Hor[30+((int(semana[tamSemana-1])-1) + 6*(int(hora[tamHora-1])-1))-1] = x[1];
                        tamHora -= 1;
                    tamHora = len(hora);
                    tamSemana -= 1;
        elif "N" in x[i]:
            semana,hora = x[i].split("N");
            tamSemana = len(semana);
            tamHora = len(hora);
            if Hor[66+((int(semana[tamSemana-1])-1) + 6*(int(hora[tamHora-1])-1))-1] != "        ":
                print(f"!(+ {x[1]} {x[i]})");
            else:
                while tamSemana > 0:
                    while tamHora > 0:
                        Hor[66+((int(semana[tamSemana-1])-1) + 6*(int(hora[tamHora-1])-1))-1] = x[1];
                        tamHora -= 1;
                    tamHora = len(hora);
                    tamSemana -= 1;
        i += 1;        
def delete():
    i = 2;
    while i < len(x):   
        if "M" in x[i]:
            semana,hora = x[i].split("M");
            tamSemana = len(semana);
            tamHora = len(hora);
            if x[1] == Hor[((int(semana[tamSemana-1])-1) + 6*(int(hora[tamHora-1])-1))-1]:
                while tamSemana > 0:
                    while tamHora > 0:
                        Hor[((int(semana[tamSemana-1])-1) + 6*(int(hora[tamHora-1])-1))-1] = "        ";
                        tamHora -= 1;
                    tamHora = len(hora);
                    tamSemana -= 1;
            else:
                print(f"!(- {x[1]} {x[i]})");
        elif "T" in x[i]:
            semana,hora = x[i].split("T");
            tamSemana = len(semana);
            tamHora = len(hora);
            if x[1] == Hor[30+((int(semana[tamSemana-1])-1) + 6*(int(hora[tamHora-1])-1))-1]:
                while tamSemana > 0:
                    while tamHora > 0:
                        Hor[30+((int(semana[tamSemana-1])-1) + 6*(int(hora[tamHora-1])-1))-1] = "        ";
                        tamHora -= 1;
                    tamHora = len(hora);
                    tamSemana -= 1;
            else:
                print(f"!(- {x[1]} {x[i]})");
        elif "N" in x[i]:
            semana,hora = x[i].split("N");
            tamSemana = len(semana);
            tamHora = len(hora);
            if x[1] == Hor[66+((int(semana[tamSemana-1])-1) + 6*(int(hora[tamHora-1])-1))-1]:
                while tamSemana > 0:
                    while tamHora > 0:
                        Hor[66+((int(semana[tamSemana-1])-1) + 6*(int(hora[tamHora-1])-1))-1] = "        ";
                        tamHora -= 1;
                    tamHora = len(hora);
                    tamSemana -= 1;
            else:
                print(f"!(- {x[1]} {x[i]})");
        i += 1;
while x != "Hasta la vista, beibe!":
    x = x.split();
    if x[0] == "?":
        print("+"+"-"*15+("+"+"-"*10)*6+"+")
        print("|"+" "*15+"| Seg      "+"| Ter      "+"| Qua      "+"| Qui      "+"| Sex      "+"| Sab      |");
        print("+"+"-"*15+("+"+"-"*10)*6+"+");
        if Hor[0]!= "        "or Hor[1]!="        "or Hor[2]!="        "or Hor[3]!="        "or Hor[4]!="        "or Hor[5]!="        ":
            print(f"| 08:00 - 08:55 | {Hor[0]} | {Hor[1]} | {Hor[2]} | {Hor[3]} | {Hor[4]} | {Hor[5]} | ");
            print("+"+"-"*15+("+"+"-"*10)*6+"+");
        if Hor[6]!= "        "or Hor[7]!="        "or Hor[8]!="        "or Hor[9]!="        "or Hor[10]!="        "or Hor[11]!="        ":
            print(f"| 08:55 - 09:50 | {Hor[6]} | {Hor[7]} | {Hor[8]} | {Hor[9]} | {Hor[10]} | {Hor[11]} | ");
            print("+"+"-"*15+("+"+"-"*10)*6+"+");
        if Hor[12]!= "        "or Hor[13]!="        "or Hor[14]!="        "or Hor[15]!="        "or Hor[16]!="        "or Hor[17]!="        ":
            print(f"| 10:00 - 10:55 | {Hor[12]} | {Hor[13]} | {Hor[14]} | {Hor[15]} | {Hor[16]} | {Hor[17]} | ");
            print("+"+"-"*15+("+"+"-"*10)*6+"+");
        if Hor[18]!= "        "or Hor[19]!="        "or Hor[20]!="        "or Hor[21]!="        "or Hor[22]!="        "or Hor[23]!="        ":
            print(f"| 10:55 - 11:50 | {Hor[18]} | {Hor[19]} | {Hor[20]} | {Hor[21]} | {Hor[22]} | {Hor[23]} | ");
            print("+"+"-"*15+("+"+"-"*10)*6+"+");
        if Hor[24]!= "        "or Hor[25]!="        "or Hor[26]!="        "or Hor[27]!="        "or Hor[28]!="        "or Hor[29]!="        ":
            print(f"| 12:00 - 12:55 | {Hor[24]} | {Hor[25]} | {Hor[26]} | {Hor[27]} | {Hor[28]} | {Hor[29]} | ");
            print("+"+"-"*15+("+"+"-"*10)*6+"+");
        if Hor[30]!= "        "or Hor[31]!="        "or Hor[32]!="        "or Hor[33]!="        "or Hor[34]!="        "or Hor[35]!="        ":
            print(f"| 12:55 - 13:50 | {Hor[30]} | {Hor[31]} | {Hor[32]} | {Hor[33]} | {Hor[34]} | {Hor[35]} | ");
            print("+"+"-"*15+("+"+"-"*10)*6+"+");
        if Hor[36]!= "        "or Hor[37]!="        "or Hor[38]!="        "or Hor[39]!="        "or Hor[40]!="        "or Hor[41]!="        ":
            print(f"| 14:00 - 14:55 | {Hor[36]} | {Hor[37]} | {Hor[38]} | {Hor[39]} | {Hor[40]} | {Hor[41]} | ");
            print("+"+"-"*15+("+"+"-"*10)*6+"+");
        if Hor[42]!= "        "or Hor[43]!="        "or Hor[44]!="        "or Hor[45]!="        "or Hor[46]!="        "or Hor[47]!="        ":
            print(f"| 14:55 - 15:50 | {Hor[42]} | {Hor[43]} | {Hor[44]} | {Hor[45]} | {Hor[46]} | {Hor[47]} | ");
            print("+"+"-"*15+("+"+"-"*10)*6+"+");
        if Hor[48]!= "        "or Hor[49]!="        "or Hor[50]!="        "or Hor[51]!="        "or Hor[52]!="        "or Hor[53]!="        ":
            print(f"| 16:00 - 16:55 | {Hor[48]} | {Hor[49]} | {Hor[50]} | {Hor[51]} | {Hor[52]} | {Hor[53]} | ");
            print("+"+"-"*15+("+"+"-"*10)*6+"+");
        if Hor[54]!= "        "or Hor[55]!="        "or Hor[56]!="        "or Hor[57]!="        "or Hor[58]!="        "or Hor[59]!="        ":
            print(f"| 16:55 - 17:50 | {Hor[54]} | {Hor[55]} | {Hor[56]} | {Hor[57]} | {Hor[58]} | {Hor[59]} | ");
            print("+"+"-"*15+("+"+"-"*10)*6+"+");
        if Hor[60]!= "        "or Hor[61]!="        "or Hor[62]!="        "or Hor[63]!="        "or Hor[64]!="        "or Hor[65]!="        ":
            print(f"| 18:00 - 18:55 | {Hor[60]} | {Hor[61]} | {Hor[62]} | {Hor[63]} | {Hor[64]} | {Hor[65]} | ");
            print("+"+"-"*15+("+"+"-"*10)*6+"+");
        if Hor[66]!= "        "or Hor[67]!="        "or Hor[68]!="        "or Hor[69]!="        "or Hor[70]!="        "or Hor[71]!="        ":
            print(f"| 19:00 - 19:50 | {Hor[66]} | {Hor[67]} | {Hor[68]} | {Hor[69]} | {Hor[70]} | {Hor[71]} | ");
            print("+"+"-"*15+("+"+"-"*10)*6+"+");
        if Hor[72]!= "        "or Hor[73]!="        "or Hor[74]!="        "or Hor[75]!="        "or Hor[76]!="        "or Hor[77]!="        ":
            print(f"| 19:50 - 20:40 | {Hor[72]} | {Hor[73]} | {Hor[74]} | {Hor[75]} | {Hor[76]} | {Hor[77]} | ");
            print("+"+"-"*15+("+"+"-"*10)*6+"+");
        if Hor[78]!= "        "or Hor[79]!="        "or Hor[80]!="        "or Hor[81]!="        "or Hor[82]!="        "or Hor[83]!="        ":
            print(f"| 20:50 - 21:40 | {Hor[78]} | {Hor[79]} | {Hor[80]} | {Hor[81]} | {Hor[82]} | {Hor[83]} | ");
            print("+"+"-"*15+("+"+"-"*10)*6+"+");
        if Hor[84]!= "        "or Hor[85]!="        "or Hor[86]!="        "or Hor[87]!="        "or Hor[88]!="        "or Hor[89]!="        ":
            print(f"| 21:40 - 22:30 | {Hor[84]} | {Hor[85]} | {Hor[86]} | {Hor[87]} | {Hor[88]} | {Hor[89]} | ");
            print("+"+"-"*15+("+"+"-"*10)*6+"+");
    elif x[0] == "+":
        add();
    elif x[0] == "-":
        delete();
    x = input()