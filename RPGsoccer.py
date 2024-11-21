#!/usr/bin/env python
# coding: utf-8

# In[39]:


import numpy as np
import random
import datetime as dt

# Este apartado debe ser completado por el estudiante
# El apartado libre usará mayormente clases y objetos
#, dado que no lo hemos usado en los otros apartados.
#También la librería numpy.
#Queremos desarrollar un juego RPG de futbol.

#Primero definimos las clases portero, defensa, medio y delantero

class Portero(object):
    def __init__(self, equipo, dorsal, parada,                  pase, pase_largo, reflejos):
        self.equipo = equipo
        self.dorsal = dorsal
        self.parada = parada
        self.pase = pase
        self.pase_largo = pase_largo
        self.reflejos = reflejos
        
    def __str__(self):
        return 'Portero({0}, {1}, {2}, {3}, {4}, {5})'                .format(self.equipo, self.dorsal,                         self.parada, self.pase,                         self.pase_largo, self.reflejos)
    
    def accion(self, skill, dado):
        """
        Given a string and an array,
        this functions gives a float as result.
        Parameters:
        ----------
        skill: string
            Name of the skill used by the player.
        dado: array of two integers e.g. [3, 4]
            Result of throwing dice.
        Returns:
        ----------
        strength: float
            Real number indicating the accuracy of an action.
        Example:
        -------
        >>> Portero.accion("pase", [3, 3])
        65.3
        """
        strength = 0.0
        power = 50.*(np.sum(dado)/12.)-25.
        if skill == "pase":
            strength = self.pase+power
        elif skill == "pase largo":
            strength = self.pase_largo+power
        elif skill == "parada":
            strength = self.parada+power
        elif skill == "reflejos":
            strength = self.reflejos+power
        
        return strength

class Defensa(object):
    def __init__(self, equipo, dorsal, entrada,                  pase, pase_largo, cabeza):
        self.equipo = equipo
        self.dorsal = dorsal
        self.entrada = entrada
        self.pase = pase
        self.pase_largo = pase_largo
        self.cabeza = cabeza
        
    def __str__(self):
        return 'Defensa({0}, {1}, {2}, {3}, {4}, {5})'                .format(self.equipo, self.dorsal,                         self.entrada, self.pase,                         self.pase_largo, self.cabeza)
    
    def accion(self, skill, dado):
        """
        Given a string and an array,
        this functions gives a float as result.
        Parameters:
        ----------
        skill: string
            Name of the skill used by the player.
        dado: array of two integers e.g. [3, 4]
            Result of throwing dice.
        Returns:
        ----------
        strength: float
            Real number indicating the accuracy of an action.
        Example:
        -------
        >>> Defensa.accion("pase", [3, 3])
        65.3
        """
        strength = 0.0
        power = 50.*(np.sum(dado)/12.)-25.
        if skill == "pase":
            strength = self.pase+power
        elif skill == "pase largo":
            strength = self.pase_largo+power
        elif skill == "entrada":
            strength = self.entrada+power
        elif skill == "cabeza":
            strength = self.cabeza+power
        
        return strength

class Medio(object):
    def __init__(self, equipo, dorsal, entrada,                  pase, chute_lejano, centro):
        self.equipo = equipo
        self.dorsal = dorsal
        self.entrada = entrada
        self.pase = pase
        self.chute_lejano = chute_lejano
        self.centro = centro
        
    def __str__(self):
        return 'Medio({0}, {1}, {2}, {3}, {4}, {5})'                .format(self.equipo, self.dorsal,                         self.entrada, self.pase,                         self.chute_lejano, self.centro)
    
    def accion(self, skill, dado):
        """
        Given a string and an array,
        this functions gives a float as result.
        Parameters:
        ----------
        skill: string
            Name of the skill used by the player.
        dado: array of two integers e.g. [3, 4]
            Result of throwing dice.
        Returns:
        ----------
        strength: float
            Real number indicating the accuracy of an action.
        Example:
        -------
        >>> Medio.accion("pase", [3, 3])
        65.3
        """
        strength = 0.0
        power = 50.*(np.sum(dado)/12.)-25.
        if skill == "pase":
            strength = self.pase+power
        elif skill == "chute lejano":
            strength = self.chute_lejano+power
        elif skill == "centro":
            strength = self.centro+power
        elif skill == "entrada":
            strength = self.entrada+power
                
        return strength
        
class Delantero(object):
    def __init__(self, equipo, dorsal, presion,                  chute, regate, cabeza):
        self.equipo = equipo
        self.dorsal = dorsal
        self.presion = presion
        self.chute = chute
        self.regate = regate
        self.cabeza = cabeza
        
    def __str__(self):
        return 'Delantero({0}, {1}, {2}, {3}, {4}, {5})'                .format(self.equipo, self.dorsal,                         self.presion, self.chute,                         self.regate, self.cabeza)
    
    def accion(self, skill, dado):
        """
        Given a string and an array,
        this functions gives a float as result.
        Parameters:
        ----------
        skill: string
            Name of the skill used by the player.
        dado: array of two integers e.g. [3, 4]
            Result of throwing dice.
        Returns:
        ----------
        strength: float
            Real number indicating the accuracy of an action.
        Example:
        -------
        >>> Delantero.accion("chute", [3, 3])
        68.3
        """
        strength = 0.0
        power = 50.*(np.sum(dado)/12.)-25.
        if skill == "chute":
            strength = self.chute+power
        elif skill == "cabeza":
            strength = self.cabeza+power
        elif skill == "regate":
            strength = self.regate+power
        elif skill == "presion":
            strength = self.presion+power
        
        return strength
    
# Ahora definimos los dados

class Dados(object):
    def __init__(self, lados=6):
        self.lados = lados
    
    def __str__(self):
        return 'Dados({0})'.format(self.sides)
    
    def lanzar(self):
        """
        Given an object Dados,
        this functions returns an array and an integer.
        Returns:
        ----------
        dado: array of two integers e.g. [3, 4]
            Result of throwing dice.
        combo: integer
            0 when dado[0] != dado[1]
            -1 when dado[0] = dado[1] < 4
            1 when dado[0] = dado[1] > 3
        Example:
        -------
        >>> Dados.lanzar()
        [4, 4], 1
        """
        dado = [0, 0]
        dado[0] = random.randint(1,self.lados)
        dado[1] = random.randint(1,self.lados)
        
        combo = 0
        if dado[0] == dado[1] and dado[0] <= 3:
            combo = -1
        elif dado[0] == dado[1] and dado[0] > 3:
            combo = 1
        
        return dado, combo
    
# Definimos el balón, cronómetro y marcador

class Balon(object):
    def __init__(self, equipo, atacante, defensor, gol):
        self.equipo = equipo
        self.atacante = atacante
        self.defensor = defensor
        self.gol = gol
    
    def __str__(self):
        return 'Balon({0}, {1}, {2}, {3})'                .format(self.equipo, self.atacante,                         self.defensor, self.gol)
    
    def cambio_pos(self):
        """
        Given an object Balon,
        this functions exchanges the values
        self.atacante and self.defensor and
        changes the team which controls the ball
        (self.equipo).
        Example:
        -------
        ball = Balon(1, 1, 11, False)
        ball.cambio_pos()
        ball --> Balon(0, 11, 1, False)
        """
        a = self.atacante
        d = self.defensor
        self.atacante = d
        self.defensor = a
        if self.equipo == 0:
            self.equipo = 1
        else:
            self.equipo = 0
        
    def cambio_at(self, newat):
        """
        Given an object Balon, and an integer,
        this functions exchanges self.atacante
        for the integer.
        Parameters:
        ----------
        newat: integer
            Number of the new attacker holding
            Balon.
        Example:
        -------
        ball = Balon(1, 1, 11, False)
        ball.cambio_at(10)
        ball --> Balon(1, 10, 11, False)
        """
        self.atacante = newat
        
    def cambio_def(self, newdef):
        """
        Given an object Balon, and an integer,
        this functions exchanges self.defensor
        for the integer.
        Parameters:
        ----------
        newdef: integer
            Number of the new defender of Balon.
        Example:
        -------
        ball = Balon(1, 1, 11, False)
        ball.cambio_def(10)
        ball --> Balon(1, 1, 10, False)
        """
        self.defensor = newdef
            
    def entra(self):
        """
        Given an object Balon,
        this functions activates the boolean
        self.gol (True).
        Example:
        -------
        ball = Balon(1, 11, 1, False)
        ball.gol()
        ball --> Balon(1, 11, 1, True)
        """
        self.gol = True

    def restart(self):
        """
        Given an object Balon,
        this functions deactivates the boolean
        self.gol (False).
        Example:
        -------
        ball = Balon(1, 11, 1, True)
        ball.restart()
        ball --> Balon(1, 11, 1, False)
        """
        self.gol = False

    def estado(self):
        """
        Given an object Balon,
        this functions prints information related to the object.
        Example:
        -------
        ball = Balon(1, 11, 1, False)
        ball.estado()
        El futbolista #1 del equipo 2 tiene el balón y es defendido \
        por el rival #1.
        """
        if self.gol:
            print("El balón se adentró en el fondo de las mallas.")
        else:
            print("El futbolista #" + str(self.atacante)                   + " del equipo " + str(self.equipo + 1) + " tiene "                  + "el balón y es defendido por el rival #"                   + str(self.defensor) + ".")
    
    
class Crono(object):
    def __init__(self, minuto):
        self.minuto = minuto
    
    def __str__(self):
        return 'Crono({0})'.format(self.minuto)
    
    def get(self):
        """
        Given an object Crono,
        this functions returns the current time.
        Example:
        -------
        time = Crono(45.2)
        t = time.get()
        print(t)
        45.2
        """
        return self.minuto
    
    def reloj(self):
        """
        Given an object Crono,
        this functions returns a clock with
        minutes and seconds.
        Example:
        -------
        time = Crono(45.25)
        time.reloj()
        Tiempo: 45:15
        """
        minutos = int(self.minuto)
        segundos = int((self.minuto - minutos) * 60.)
        print("Tiempo: " + str(minutos) + ":"               + str(segundos))
        
    def lapso(self, proc):
        """
        Given an object Crono, and a string,
        this functions adds time due to an action.
        Parameters:
        ----------
        proc: string
            Action of the player
        Example:
        -------
        time = Crono(45.25)
        time.lapso("pase") --> Crono(45.25 + 0.25)
        """
        if proc == "pase":
            dt = 0.25
        elif proc == "pase largo":
            dt = 0.50
        elif proc == "centro":
            dt = 0.50
        elif proc == "regate":
            dt = 0.25
        elif proc == "chute":
            dt = 0.25
        elif proc == "chute lejano":
            dt = 0.50
        
        self.minuto += dt
        
    
class Marcador(object):
    def __init__(self, local, visitante, quiniela):
        self.local = local
        self.visitante = visitante
        self.quiniela = quiniela
    
    def __str__(self):
        return 'Marcador({0}, {1}, {2}, {3})'                 .format(self.local, self.visitante,                         self.quiniela)
    
    def golazo(self):
        """
        Given an object Marcador,
        this functions prints a message with
        the new score of the game, after a goal.
        Example:
        -------
        score = Marcador(1, 0, "1")
        score.golazo()
        ¡Gooooooool! Ahora el resultado es de 1 - 0.
        """
        print("¡Gooooooool! Ahora el resultado es de "               + str(self.local) + " - "               + str(self.visitante))
        
    def gol_loc(self):
        """
        Given an object Marcador,
        this functions adds a goal to the home team.
        Example:
        -------
        score = Marcador(1, 0, "1")
        score.gol_loc() --> Marcador(2, 0, "1")
        """
        self.local += 1
        if self.local > self.visitante:
            self.quiniela = "1"
        elif self.local == self.visitante:
            self.quiniela = "X"
    
    def gol_vis(self):
        """
        Given an object Marcador,
        this functions adds a goal to the visitor team.
        Example:
        -------
        score = Marcador(1, 0, "1")
        score.gol_vis() --> Marcador(1, 1, "X")
        """
        self.visitante += 1
        if self.local < self.visitante:
            self.quiniela = "2"
        elif self.local == self.visitante:
            self.quiniela = "X"
    
    def final(self):
        """
        Given an object Marcador,
        this functions prints the final result of the game.
        Also, prints the date and the result into an external file
        called Final-Results.txt.
        Example:
        -------
        score = Marcador(1, 0, "1")
        score.final()
        El resultado final es 1 - 0
        in Final-Results.txt --> 24-10-29 1 - 0 en la quiniela es un 1
        """
        print("El resultado final es " + str(self.local) + " - "               + str(self.visitante))
        with open("Final-Results.txt", "a") as file:
              file.write(str(dt.date.today()) + "  " + str(self.local)                          + " - " + str(self.visitante)                         + " en la quiniela es un "                          + str(self.quiniela) + "\n")

# Ahora que tenemos todos los elementos del juego, empezamos.

def generar(equipo, formacion):
    """
    Given an integer (team) and a list of 3 integers (e.g. 4 4 2),
    this function creates 11 players for a team using the Portero,
    Defensa, Medio, and Delantero classes and producing randomized
    values of their 4 skills.
    Parameters:
    -------
    equipo: integer
        Team identifier (0 or 1)
    formacion: list of 3 integers (e.g. [4, 4, 2]
        Players distribution [defenders, midcenters, strikers].
    Returns:
    -------
    futbolistas: list of NoneType (objects)
        List of players of the team (equipo), ordered by number 
        (1 to 11) with 4 randomly generated skills (depending
        the kind of player).
    Example:
    -------
    equipo1 = generar(0, [4, 4, 2])
    """
    futbolistas = []
    alea = np.random.normal(0, 4, size=(4))
    numero = 1
    futbolistas.append(Portero(equipo, numero, 75 + alea[0],                               70 + alea[1], 65 + alea[2],                              55 + alea[3]))
    for i in range(int(formacion[0])):
        alea = np.random.normal(0, 4, size=(4))
        numero += 1
        futbolistas.append(Defensa(equipo, numero, 75 + alea[0],                                         65 + alea[1], 55 + alea[2],                                         60 + alea[3]))
    
    for i in range(int(formacion[1])):
        alea = np.random.normal(0, 4, size=(4))
        numero += 1
        futbolistas.append(Medio(equipo, numero, 60 + alea[0],                                         75 + alea[1], 55 + alea[2],                                         65 + alea[3]))
    
    for i in range(int(formacion[2])):
        alea = np.random.normal(0, 4, size=(4))
        numero += 1
        futbolistas.append(Delantero(equipo, numero, 55 + alea[0],                                        75 + alea[1], 65 + alea[2],                                         60 + alea[3]))
    
    return futbolistas
        

def elec(pos):
    """
    Given the position of the player (string),
    this function prints a list of available offensive
    actions.
    Example:
    -------
    >>>elec("portero")
     pase
     pase largo
    """
    if pos == "portero":
        print(" pase ")
        print(" pase largo ")
    elif pos == "defensa":
        print(" pase ")
        print(" pase largo" )
    elif pos == "medio":
        print(" pase ")
        print(" chute lejano ")
        print(" centro ")
    elif pos == "delantero":
        print(" chute ")
        print(" regate ")


def jugada(eqat, pos, jat):
    """
    Given the team (integer), a list of strings with
    the position of the players of the team, and the 
    number of the attacker player, this function 
    prints a message for the player asking for the
    next action.
    Parameters:
    -------
    eqat: integer
        Attacking team identity (0 or 1)
    pos: list of strings
        List of descriptors for players 
    jat: integer
        Number of the attacking player
    Example:
    -------
    jugada(0, pos, 10)
    Jugador 1, su delantero #10 está atacando.
    ¿Qué acción escoge?
     chute
     regate
    """
    print("Jugador " + str(eqat + 1) + " , su "           + str(pos[jat-1]) + " #" + str(jat)           + " está atacando. ¿Qué acción escoge?")
    elec(pos[jat-1])


def contra(acto, posacto, eqdef, pos, jdef):
    """
    Given the offensive action of the rival, the position of
    the offensive player, the defensive team identifyer, the
    position list and the number of the defensive player, this
    function prints asking the player which player is going to 
    defend and what action will try.
    Parameters:
    --------
    acto: string
        Action of the attacker player.
    posacto: string
        Position of the attacker player (e.g. "defensa")
    eqdef: integer
        Defending team identity (0 or 1)
    pos: list of strings
        List of descriptors for players 
    jdef: integer
        Number of the defending player
    Returns:
    -------
    actodef: string
        Action of the defense. 
    Example:
    -------
    actodef = contra("pase", "portero", 0, pos, 11)
    Jugador 1, ¿qué delantero escoges para presionar?
    [10, 11]
    """
    if posacto == "portero" or posacto == "defensa":
        actodef = "presion"
        print("Jugador " + str(eqdef + 1) + ", ¿qué delantero "               "escoges para presionar?")
        print(str([i + 1 for i in range(len(pos))                    if pos[i] == "delantero"]))
    elif posacto == "medio":
        actodef = "entrada"
        print("Jugador " + str(eqdef + 1) + ", ¿qué medio "               "escoges para defender?")
        print(str([i + 1 for i in range(len(pos))                    if pos[i] == "medio"]))
    elif posacto == "delantero":
        actodef = "entrada"
        print("Jugador " + str(eqdef + 1) + ", ¿qué defensa "               "escoges para defender?")
        print(str([i + 1 for i in range(len(pos))                    if pos[i] == "defensa"]))
    
    return actodef
    
def criterio(azar, potencia, jug, intento):
    """
    Given an integer (azar = comboat - combodef), a real
    number (potencia = strengthat - strengthdef), a string
    with the kind of player, and a string with the 
    offensive try, this function provides a string with 
    the descriptor of the final consequence of the game.
    Parameters:
    --------
    azar: integer
        Value from -2 to +2 (comboat - combodef, dice)
    potencia: float
        Value of the difference in strength of the attacker
        and the defender
    jug: string
        Descriptor of the kind of offensive player
    intento: string
        Descriptor of the offensive action
    Returns:
    -------
    ocurre: string
        Consequence of the individual action between defender and
        attacker
    Example:
    -------
    consecuencia = criterio(-1, -3.43, "delantero", "chute")
    print(consecuencia)
    medrival (the ball goes to a rival middle-center)
    """
    if jug == "portero" and intento == "pase":
        if azar == -2:
            ocurre = "golrival"
        elif azar == -1:
            ocurre = "1vs1rival"
        elif azar == 0:
            if potencia >= 0:
                ocurre = "pasedef"
            else:
                ocurre = "robo"
        elif azar > 0:
            ocurre = "pasemed"
    elif jug == "portero" and intento == "pase largo":
        if azar == -2:
            ocurre = "golrival"
        elif azar == -1:
            ocurre = "1vs1rival"
        elif azar == 0:
            if potencia >= 0:
                ocurre = "pasemed"
            else:
                ocurre = "robo"
        elif azar == 1:
            ocurre = "pasedel"
        elif azar == 2:
            ocurre = "1vs1"
    elif jug == "defensa":
        if azar == -2:
            ocurre = "1vs1rival"
        elif azar == -1:
            ocurre = "delrival"
        elif azar == 0:
            if potencia >= 0 and intento == "pase":
                ocurre = "pasemed"
            elif potencia >= 0 and intento == "pase largo":
                ocurre = "pasedel"
            else:
                ocurre = "robo"
        elif azar == 1 and intento == "pase":
            ocurre = "pasedel"
        elif azar == 1 and intento == "pase largo":
            ocurre = "1vs1"
        elif azar == 2:
            ocurre = "1vs1"
    elif jug == "medio" and intento == "pase":
        if azar < 0:
            ocurre = "delrival"
        elif azar == 0:
            if potencia >= 0:
                ocurre = "pasedel"
            else:
                ocurre = "robo"
        elif azar > 0:
            ocurre = "1vs1"
    elif jug == "medio" and intento == "chute lejano":
        if azar < 0:
            ocurre = "delrival"
        elif azar == 0:
            if potencia >= 0:
                ocurre = "chute lejano 2"
            else:
                ocurre = "robo"
        elif azar > 0:
            ocurre = "chute 2"
    elif jug == "medio" and intento == "centro":
        if azar < 0:
            ocurre = "delrival"
        elif azar == 0:
            if potencia >= 0:
                ocurre = "cabvsdef"
            else:
                ocurre = "robo"
        elif azar > 0:
            ocurre = "cabvspor"
    elif jug == "delantero" and intento == "regate":
        if azar < 0:
            ocurre = "medrival"
        elif azar == 0:
            if potencia >= 0:
                ocurre = "1vs1"
            else:
                ocurre = "robo"
        elif azar > 0:
            ocurre = "gol"
    elif jug == "delantero" and intento == "chute":
        if azar < 0:
            ocurre = "medrival"
        elif azar == 0:
            if potencia >= 0:
                ocurre = "chute 2"
            else:
                ocurre = "robo"
        elif azar > 0:
            ocurre = "gol"
    
    return ocurre

def consec(fact, eqat, eqdef, atac, defe, score, ball, posa, posd):
    """
    This function is not finished (but, the game can work without
    all the conditions).
    
    Given the name of the consequence (string), the identifyer of
    the attacker, defender, teams, and the objects of the game 
    (score, ball), this function make changes depending on the
    descriptor of the consequence. (e.g. a goal should affect the 
    score, the position of the ball, etc.)
    Parameters: 
    -------
    fact: string
        Descriptor of the consequence 
    atac: integer
        Number of the attacker
    defe: integer
        Number of the defender
    eqat: integer
        Offensive team (0 or 1)
    eqdef: integer
        Defensive team (0 or 1)
    score: NoneType (object)
        Marcador-type object, scoring board
    ball: NoneType (object)
        Balon-type object, ball
    posa: string
        Position of the attacker 
    posd: string
        Position of the defender
    Returns:
    -------
    New versions of atac, defe, eqat, eqdef, score, ball
    Example:
    -------
    atac, defe, eqat, eqdef,\
    score, ball = consec(fact, atac, defe, eqat, eqdef,\
                         score, ball, posa, posb)
    """
    if fact == "golrival":
        print("¡El balón rebota en el rival y...!")
        ball.cambio_pos()
        exe = eqat
        eqat = eqdef
        eqdef = exe
        ball.entra()
        ball.estado()
        if eqat == 0:
            score.gol_loc()
        else:
            score.gol_vis()
        score.golazo()
        ball.restart()
        atac = 1
        ball.cambio_at(atac)
        defe = 11
        ball.cambio_def(defe)
    elif fact == "gol":
        ball.entra()
        ball.estado()
        if eqat == 0:
            score.gol_loc()
        else:
            score.gol_vis()
        score.golazo()
        ball.restart()
        ball.cambio_pos()
        exe = eqat
        eqat = eqdef
        eqdef = exe
        atac = 1
        defe = 11
    elif fact == "pasedef":
        print("Jugador " + str(eqat + 1) + ", ¿qué defensa "               "recibe el pase?")
        print(str([i + 1 for i in range(len(posa))                    if posa[i] == "defensa"]))
        atac = int(input())
        ball.cambio_at(atac)
    elif fact == "pasemed":
        print("Jugador " + str(eqat + 1) + ", ¿qué medio "               "recibe el pase?")
        print(str([i + 1 for i in range(len(posa))                    if posa[i] == "medio"]))
        atac = int(input())
        ball.cambio_at(atac)
    elif fact == "pasedel":
        print("Jugador " + str(eqat + 1) + ", ¿qué delantero "               "recibe el pase?")
        print(str([i + 1 for i in range(len(posa))                    if posa[i] == "delantero"]))
        atac = int(input())
        ball.cambio_at(atac)
    elif fact == "robo":
        print("Se produjo el robo, el balón cambia de equipo.")
        exj = atac
        atac = defe
        defe = exj
        
        exe = eqat
        eqat = eqdef
        eqdef = exe
        
        ball.cambio_pos()
        ball.cambio_at(atac)
        ball.cambio_def(defe)
        
    elif fact == "delrival":
        print("Jugada con mucho riesgo, el balón va al delantero rival.")
        atac = 11
        defe = 2
        
        exe = eqat
        eqat = eqdef
        eqdef = exe
        
        ball.cambio_pos()
        ball.cambio_at(atac)
        ball.cambio_def(defe)
    elif fact == "medrival":
        print("Se precipita y le da el balón al medio rival.")
        atac = 7
        defe = 7
        
        exe = eqat
        eqat = eqdef
        eqdef = exe
        
        ball.cambio_pos()
        ball.cambio_at(atac)
        ball.cambio_def(defe)
             
    return eqat, eqdef, atac, defe, score, ball

def RPGsoccer():
    """
    Main RPGsoccer game. The function interacts with the players like
    in a role game. The players decide the length of the game in time,
    the number of football players, defensive, offensive, they decide 
    what to do next and the dice decide what consequences occur along
    the game. RPGsoccer is a soccer game based in objects like 
    goalkeeper (Portero), defenders (Defensa), clock (Crono), scoring
    board (Marcador), ball (Balon), etc. and uses random number 
    generators to make the experience new every game. New players with
    new skills, throwing dice every turn.
    Example:
    ------
    RPGsoccer()
    """
    print("Bienvenidos a RPG soccer. ¿Cuántos minutos desean jugar?")
    tiempo_total = input()

    print("Jugador 1, ¿qué formación desea usar?     e.g. 3 5 2, 4 3 3, 5 4 1 (Solo tres enteros)")
    formacion1 = list(map(int, input().split()))
    
    if sum(formacion1) != 10:
        raise Exception("Lo siento, necesitas 10 jugadores")
    
    equipo1 = generar(0, formacion1)
    
    posicion1 = ["portero"]    
    [posicion1.append("defensa") for i in range(formacion1[0])]
    [posicion1.append("medio") for i in range(formacion1[1])]
    [posicion1.append("delantero") for i in range(formacion1[2])]
    
    print("Jugador 2, ¿qué formación desea usar?     e.g. 3 5 2, 4 3 3, 5 4 1 (Solo tres enteros)")
    formacion2 = list(map(int, input().split()))
    
    if sum(formacion2) != 10:
        raise Exception("Lo siento, necesitas 10 jugadores")
    
    posicion2 = ["portero"]
    
    [posicion2.append("defensa") for i in range(formacion2[0])]
    [posicion2.append("medio") for i in range(formacion2[1])]
    [posicion2.append("delantero") for i in range(formacion2[2])]
              
    equipo2 = generar(1, formacion2)
              
    print("Lanzamos una moneda, jugador 1, ¿cara o cruz?")
    guess = input()
    if guess != "cara" and guess != "cruz":
        raise Exception("Escribe cara o escribe cruz")
    moneda = random.randint(0,1)
    
    if guess == "cara" and moneda == 0:
        starts = 0
    elif guess == "cara" and moneda == 1:
        starts = 1
    elif guess == "cruz" and moneda == 0:
        starts = 1
    elif guess == "cruz" and moneda == 1:
        starts = 0
    
    print("¡Empieza el partido! El balón es para jugador "           + str(starts + 1))

#Inicializamos algunos objetos

    atacante = 1               #El balon empieza en el portero atacante
    defensor = 11
    balon = Balon(starts, atacante, defensor, False)   
    tiempo = Crono(0.0)
    marcador = Marcador(0, 0, "X")
    
#Empezamos el loop del juego
    t = tiempo.get()
    print(str(t))
    eqataque = starts
    dadosat = [0, 0]
    dadosdef = [0, 0]
        
    while t <= float(tiempo_total):
        tiempo.reloj()
        
        if eqataque == 0:
            eqdefensa = 1
            posataque = posicion1
            posdefensa = posicion2
            equipoat = equipo1
            equipodef = equipo2
        else:
            eqdefensa = 0
            posataque = posicion2
            posdefensa = posicion1
            equipoat = equipo2
            equipodef = equipo1
        
        jugada(eqataque, posataque, atacante)
        actoat = input()
        actodef = contra(actoat, posataque[atacante-1],                          eqdefensa, posdefensa, defensor)
        defensor = int(input())
        
        balon = Balon(eqataque, atacante, defensor, False)
        balon.estado()
        
        print("Jugador " + str(eqataque + 1) + ", lance los dados.")
        input()
        dadosat, comboat = Dados().lanzar()
        print(str(dadosat))
        print("Jugador " + str(eqdefensa + 1) + ", lance los dados.")
        input()
        dadosdef, combodef = Dados().lanzar()
        print(str(dadosdef))
        
        F_at = equipoat[atacante-1].accion(actoat, dadosat)
        F_def = equipodef[defensor-1].accion(actodef, dadosdef)
        dF = F_at - F_def
        dcombo = comboat - combodef
        
        hecho = criterio(dcombo, dF, posataque[atacante - 1], actoat)
        eqataque, eqdefensa, atacante,         defensor, marcador, balon = consec(hecho, eqataque, eqdefensa,                                            atacante, defensor, marcador,                                            balon, posataque, posdefensa)
        if hecho == "1vs1" or hecho == "1vs1rival":
            if hecho == "1vs1rival":
                print("¡Peligrosa pérdida de balón!")
                exe = eqataque
                eqataque = eqdefensa
                eqdefensa = exe
                balon.cambio_pos()
                atacante = defensor
                balon.cambio_at(atacante)
            
            if actoat != "regate":
                atacante = 11
                balon.cambio_at(atacante)
            defensor = 1
            balon.cambio_def(defensor)
            
            actoat = "chute"
            actodef = "reflejos"
            
            print("Tenemos un 1 vs 1 entre el delantero y el portero.")
            print("Jugador " + str(eqataque + 1) + ", lance los dados.")
            input()
            dadosat, comboat = Dados().lanzar()
            print(str(dadosat))
            print("Jugador " + str(eqdefensa + 1) + ", lance los dados.")
            input()
            dadosdef, combodef = Dados().lanzar()
            print(str(dadosdef))
            
            F_at = equipoat[atacante-1].accion(actoat, dadosat)
            F_def = equipodef[defensor-1].accion(actodef, dadosdef)
            dF = F_at - F_def
            dcombo = comboat - combodef
            
            if dcombo > 0 or dF > 0:
                hecho = "gol"
            else:
                print("¡Impresionantes reflejos del portero, voló!")
                hecho = "robo"
            
            eqataque, eqdefensa, atacante,             defensor, marcador, balon = consec(hecho, eqataque, eqdefensa,                                            atacante, defensor, marcador,                                            balon, posataque, posdefensa)
        elif hecho == "chute 2":
            print("El balón va hacia el portero.")
            print("¿La parará?")
            defensor = 1
            actodef = "parada"
            print("Jugador " + str(eqataque + 1) + ", lance los dados.")
            input()
            dadosat, comboat = Dados().lanzar()
            print(str(dadosat))
            print("Jugador " + str(eqdefensa + 1) + ", lance los dados.")
            input()
            dadosdef, combodef = Dados().lanzar()
            print(str(dadosdef))
            
            F_at = equipoat[atacante-1].accion(actoat, dadosat)
            F_def = equipodef[defensor-1].accion(actodef, dadosdef)
            dF = F_at - F_def
            dcombo = comboat - combodef
            
            if dcombo > 0 or dF > 0:
                hecho = "gol"
            else:
                print("¡Paradón de categoría!")
                hecho = "robo"
            
            eqataque, eqdefensa, atacante,             defensor, marcador, balon = consec(hecho, eqataque, eqdefensa,                                            atacante, defensor, marcador,                                            balon, posataque, posdefensa)
                
        elif hecho == "chute lejano 2":
            print("El balón supera al medio y va hacia el defensor")
            print("¿La parará?")
            defensor = 2
            actodef = "entrada"
            print("Jugador " + str(eqataque + 1) + ", lance los dados.")
            input()
            dadosat, comboat = Dados().lanzar()
            print(str(dadosat))
            print("Jugador " + str(eqdefensa + 1) + ", lance los dados.")
            input()
            dadosdef, combodef = Dados().lanzar()
            print(str(dadosdef))
            
            F_at = equipoat[atacante-1].accion(actoat, dadosat)
            F_def = equipodef[defensor-1].accion(actodef, dadosdef)
            dF = F_at - F_def
            dcombo = comboat - combodef
            
            if dcombo > 0:
                print("El balón rebota en el defensa, confunde al portero ")
                print("y ¡goooooool!")
                hecho = "gol"
            elif dcombo == 0 and dF >= 0:
                print ("El balón sigue adelante hacia el portero.")
                print ("¿La parará?")
                defensor = 1
                actodef = "parada"
                print("Jugador " + str(eqataque + 1) + ", lance los dados.")
                input()
                dadosat, comboat = Dados().lanzar()
                print(str(dadosat))
                print("Jugador " + str(eqdefensa + 1) + ", lance los dados.")
                input()
                dadosdef, combodef = Dados().lanzar()
                print(str(dadosdef))
            
                F_at2 = equipoat[atacante-1].accion(actoat, dadosat)
                F_def2 = equipodef[defensor-1].accion(actodef, dadosdef)
                dF2 = F_at2 - F_def2
                dcombo2 = comboat - combodef
                
                if dcombo2 > 0 or dF2 > 0:
                    hecho = "gol"
                else:
                    print("¡Parada fácil, tenía tiempo de verla venir!")
                    hecho = "robo"
            else:
                print("¡Balón interceptado por el defensa!")
                hecho = "robo"
        
            eqataque, eqdefensa, atacante,             defensor, marcador, balon = consec(hecho, eqataque, eqdefensa,                                            atacante, defensor, marcador,                                            balon, posataque, posdefensa)    
                
                
        elif hecho == "cabvsdef" or hecho == "cabvspor":
            hecho2 = "nada"
            if hecho == "cabvsdef":
                atacante = 11
                balon.cambio_at(atacante)
                defensor = 2
                balon.cambio_def(defensor)
                actoat = "cabeza"
                actodef = "cabeza"
                
                print("¡Saltan dos jugadores a cabecear la pelota!")
                print("Jugador " + str(eqataque + 1) + ", lance los dados.")
                input()
                dadosat, comboat = Dados().lanzar()
                print(str(dadosat))
                print("Jugador " + str(eqdefensa + 1) + ", lance los dados.")
                input()
                dadosdef, combodef = Dados().lanzar()
                print(str(dadosdef))
            
                F_at = equipoat[atacante-1].accion(actoat, dadosat)
                F_def = equipodef[defensor-1].accion(actodef, dadosdef)
                dF = F_at - F_def
                dcombo = comboat - combodef
                
                if dcombo > 0 or dF > 0:
                    hecho2 = "next"
                else:
                    print("¡Interceptación del defensa!")
                    hecho = "robo"
                
                actoat = "centro"
                
            elif hecho == "cabvspor":
                hecho2 = "next"
            
            if hecho2 == "next":
                atacante = 11
                balon.cambio_at(atacante)
                defensor = 1
                balon.cambio_def(defensor)
                actoat = "cabeza"
                actodef = "reflejos"
                
                print("¡El remate de cabeza se dirige a portería!")
                print("Jugador " + str(eqataque + 1) + ", lance los dados.")
                input()
                dadosat, comboat = Dados().lanzar()
                print(str(dadosat))
                print("Jugador " + str(eqdefensa + 1) + ", lance los dados.")
                input()
                dadosdef, combodef = Dados().lanzar()
                print(str(dadosdef))
            
                F_at = equipoat[atacante-1].accion(actoat, dadosat)
                F_def = equipodef[defensor-1].accion(actodef, dadosdef)
                dF = F_at - F_def
                dcombo = comboat - combodef
                
                if dcombo > 0 or dF > 0:
                    print("¡Cabezazo antológico!")
                    hecho = "gol"
                else:
                    print("¡Vuela el portero con unos reflejos felinos!")
                    hecho = "robo"
                
                actoat = "centro"
                
            
            eqataque, eqdefensa, atacante,             defensor, marcador, balon = consec(hecho, eqataque, eqdefensa,                                            atacante, defensor, marcador,                                            balon, posataque, posdefensa)
                
            
        tiempo.lapso(actoat)
        t = tiempo.get()
    
    print("¡Y el árbitro pita el final del partido!")
    marcador.final()


# In[ ]:


RPGsoccer()


# In[ ]:




