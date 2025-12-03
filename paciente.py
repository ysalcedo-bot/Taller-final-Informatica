# model/paciente.py

class Paciente:

    # ---------------- CONSTRUCTOR ----------------
    def __init__(self, nombre, id, edad, bpm, spo2, temperatura):
        self.set_nombre(nombre)
        self.set_id(id)
        self.set_edad(edad)
        self.set_bpm(bpm)
        self.set_spo2(spo2)
        self.set_temperatura(temperatura)

    # ---------------- GETTERS ----------------
    def get_nombre(self):
        return self._nombre

    def get_id(self):
        return self._id

    def get_edad(self):
        return self._edad

    def get_bpm(self):
        return self._bpm

    def get_spo2(self):
        return self._spo2

    def get_temperatura(self):
        return self._temperatura

    # ---------------- SETTERS con validaciones ----------------
    def set_nombre(self, nombre):
        if not isinstance(nombre, str) or nombre.strip() == "":
            raise ValueError("El nombre no puede estar vacío.")
        self._nombre = nombre

    def set_id(self, id):
        if not isinstance(id, str) or id.strip() == "":
            raise ValueError("El ID no puede estar vacío.")
        self._id = id

    def set_edad(self, edad):
        if not isinstance(edad, int) or edad <= 0:
            raise ValueError("Edad inválida.")
        self._edad = edad

    def set_bpm(self, bpm):
        if not isinstance(bpm, (int, float)) or bpm <= 0:
            raise ValueError("BPM inválido.")
        self._bpm = bpm

    def set_spo2(self, spo2):
        if not isinstance(spo2, (int, float)) or not (0 <= spo2 <= 100):
            raise ValueError("SpO₂ debe estar entre 0 y 100.")
        self._spo2 = spo2

    def set_temperatura(self, temperatura):
        if not isinstance(temperatura, (int, float)):
            raise ValueError("Temperatura inválida.")
        self._temperatura = temperatura

    # ---------------- MÉTODO DE LÓGICA BIOMÉDICA ----------------
    def calcular_riesgo(self):

        # Crítico
        if (self._spo2 < 90 or 
            self._bpm < 40 or self._bpm > 150 or 
            self._temperatura >= 40):
            return "Crítico"

        # Alerta
        if ((90 <= self._spo2 < 94) or 
            (50 > self._bpm or self._bpm > 120) or 
            self._temperatura > 38):
            return "Alerta"

        # Normal
        return "Normal"

