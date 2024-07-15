import customtkinter

def mostrar_error():
        janela_error = customtkinter.CTk()

        janela_error.geometry('400x100')

        texto_error = customtkinter.CTkLabel(janela_error,text='DIGITE APENAS VALORES NUMERICOS')
        texto_error.pack(padx=10,pady=10)

        botao_ok = customtkinter.CTkButton(janela_error,text='ok',command=janela_error.destroy)
        botao_ok.pack(padx=10,pady=10)

        janela_error.mainloop()

texto_imc = None
def calcular():
    global texto_imc
    try:
        a= float(altura.get().replace(',','.'))
        p= float(peso.get().replace(',','.'))
        
        if texto_imc is not None:
            texto_imc.destroy()

        imc = p/(a*a)
        if imc > 18.5 and imc < 24.9:
            texto_imc = customtkinter.CTkLabel(janela,text=f'Seu IMC é {imc:.3f}, sua classificação é : PESO NORMAL.',text_color='green')

            print(f'Seu IMC é {imc:.3f}, sua classificação é : PESO NORMAL.')
        elif imc > 24.9 and imc < 29.9 :
            texto_imc = customtkinter.CTkLabel(janela,text=f'Seu IMC é {imc:.3f}, sua classificação é :  SOBREPESO.',text_color='blue')
            
            print(f'Seu IMC é {imc:.3f}, sua classificação é : SOBREPESO.')
        elif imc > 30 and imc < 34.9:
            texto_imc = customtkinter.CTkLabel(janela,text=f'Seu IMC é {imc:.3f}, sua classificação é : OBESIDADE GRAU I.',text_color='yellow')
            print(f'Seu IMC é {imc:.3f}, sua classificação é : OBESIDADE GRAU I.')
        elif imc > 35 and imc < 39.9 :
            texto_imc = customtkinter.CTkLabel(janela,text=f'Seu IMC é {imc:.3f}, sua classificação é : OBESIDADE GRAU II.',text_color='orange')
            print(f'Seu IMC é {imc:.3f}, sua classificação é : OBESIDADE GRAU II.')
        elif imc < 18.5 :
            texto_imc = customtkinter.CTkLabel(janela,text=f'Seu IMC é {imc:.3f}, sua classificação é : BAIXO PESO.')
            print(f'Seu IMC é {imc:.3f}, sua classificação é : BAIXO PESO.')
        else:
            texto_imc = customtkinter.CTkLabel(janela,text=f'Seu IMC é {imc:.3f}, sua classificação é : OBESIDADE GRAU III.',text_color='red')
            print(f'Seu IMC é {imc:.3f}, sua classificação é : OBESIDADE GRAU III.')

        texto_imc.pack(padx=10,pady=10)
    except:

        mostrar_error()

        



    

janela = customtkinter.CTk()
janela.geometry('400x290')

texto = customtkinter.CTkLabel(janela,text='Calculo IMC')
texto.pack(padx=10,pady=10)

texto_linha2 = customtkinter.CTkLabel(janela,text='digitar altura em metro')
texto_linha2.pack(padx=1,pady=1)

altura = customtkinter.CTkEntry(janela,placeholder_text='Altura')
altura.pack(padx=1,pady=1)

peso = customtkinter.CTkEntry(janela,placeholder_text='Peso')
peso.pack(padx=10,pady=10)

botao = customtkinter.CTkButton(janela,text='Calcular',command=calcular)
botao.pack(padx=10,pady=10)


    







janela.mainloop()

# 1. Interface Gráfica:
# ○ Criar uma janela principal.
# ○ Adicionar campos de entrada para o peso (em kg) e altura (em metros(exemplo:
# 1.70, 1.80)
# ○ Adicionar um botão para calcular o IMC.
# ○ Adicionar um campo para exibir o resultado do IMC.
# ○ Adicionar um campo para exibir a categoria do IMC
# i. Muito abaixo do peso
# ii. Abaixo do peso
# iii. Peso normal
# iv. Acima do peso
# v. Obesidade I
# vi. Obesidade II
# vii. Obesidade III
# ○ Personalize as cores da categoria para que tudo fique mais intuitivo(coloque
# cores diferentes para cada nível
# i. (ex:vá de branco para vermelho, de acordo com o nível de obesidade)