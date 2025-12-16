#Considerando a lista inicial de eventos, crie um programa que permita ao organizador ordená-los, de forma que a lista final siga a sequência correta.
import os
os.system('cls')

eventos_registrados = ['Encerramento', 'Palestra 3', 'Palestra 2', 'Abertura']
eventos_registrados.reverse()
print(f"Ordem corrigida: {eventos_registrados}")