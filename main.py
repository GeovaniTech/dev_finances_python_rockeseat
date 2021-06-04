from PyQt5 import uic, QtWidgets
from PyQt5 import QtCore
from datetime import date


class FrmPrincial:
    def __init__(self):
        # Definindo dados['saldo']
        dados['saldo'] = 0
        # Exibindo FrmPrincipal
        frm_principal.show()

        # Definindo largura de cada coluna da Tabela
        frm_principal.tabela.setColumnWidth(0, 309)
        frm_principal.tabela.setColumnWidth(1, 115)
        frm_principal.tabela.setColumnWidth(2, 115)

        # Deixando invisivel a coluna numérica da esquerda
        frm_principal.tabela.verticalHeader().setVisible(False)

        # insirindo data atual
        frm_remover_alterar_transacao.data.setDate(data_atual)
        frm_transacoes.textdata.setDate(data_atual)

        # Botões do FrmPrincipal
        frm_principal.btntransactions.clicked.connect(FrmPrincial.btn_transactions_clicked)
        frm_principal.btnsaldo.clicked.connect(FrmPrincial.btn_adicionarsaldo_clicked)
        frm_principal.btnremover.clicked.connect(FrmPrincial.btn_remover_alterar_clicked)

        # Chamando FrmRemover_Alterar
        FrmRemover_Alterar()


    def FecharSaldo(self):
        # Fechando FrmSaldo
        frm_saldo.close()

        # Limpando Linha Saldo
        frm_saldo.textsaldo.clear()


    def FecharTransactions(self):
        # Fechando FrmTransactions
        frm_transacoes.close()

        # Limpando as Linhas Descrição, Valor e Data
        frm_transacoes.textdescricao.clear()
        frm_transacoes.textvalor.clear()
        frm_transacoes.textdata.clear()


    def btn_adicionarsaldo_clicked(self):
        # Abrindo FrmAdicionarSaldo
        frm_saldo.show()

        # Cliques dos Botões do Formulário
        frm_saldo.btnsalvar.clicked.connect(FrmPrincial.adicionar_saldo)
        frm_saldo.btncancelar.clicked.connect(FrmPrincial.FecharSaldo)

        # Colocando cor padrão da Mensagem de Erro e da Borda da Linha
        frm_saldo.msgerror.setStyleSheet("color: #F0F0F0;")
        frm_saldo.textsaldo.setStyleSheet("background-color: rgb(255,255,255); border-radius: 2px; border: 2px solid white;")


    def btn_transactions_clicked(self):
        # Abrindo FrmTransactions
        frm_transacoes.show()

        # Cliques dos Botões do Formulário
        frm_transacoes.btncancelar.clicked.connect(FrmPrincial.FecharTransactions)
        frm_transacoes.btnsalvar.clicked.connect(FrmPrincial.transactions)

        # Colocando cor Padrão das Mensagens de Erro e da Borda das Linhas
        frm_transacoes.textdescricao.setStyleSheet("background-color: rgb(255, 255, 255); border-radius: 2px; border 2px solid white")
        frm_transacoes.textvalor.setStyleSheet("background-color: rgb(255, 255, 255); border-radius: 2px; border: 2px solid white;")
        frm_transacoes.lblerror.setStyleSheet('color: rgb(240, 242, 245);')


    def btn_remover_alterar_clicked(self):
        # Abrindo FrmRemover/Alterar Transactions
        frm_remover_alterar_transacao.show()


    def adicionar_saldo(self):
        # Informando que variável saldo é igual a linha de Texto Saldo
        saldo = frm_saldo.textsaldo.text()

        # Verificando se saldo é número
        if saldo.isnumeric():
            #Transformando variável saldo em número inteiro
            saldo = int(frm_saldo.textsaldo.text())

            # Informando que agora dados['saldo'] é igual a variável saldo
            dados['saldo'] = saldo

            # Fazendo os calculos da lblTotal_Saídas e lblTotal_Final do FrmPrincipal
            frm_principal.lblentrada.setText(lang.toString(saldo * 0.01, 'f', 2))
            frm_principal.lbltotal.setText(lang.toString((dados['saldo'] - sum(gastos_saidas)) * 0.01, 'f', 2))

            # Limpando linha de Texto Saldo
            frm_saldo.textsaldo.clear()

            # Fechando FrmSaldo
            frm_saldo.close()

        # Verificando se a linha de Texto Saldo está vazia
        elif saldo == "":
            frm_saldo.msgerror.setText("Digite um Valor!")
            frm_saldo.msgerror.setStyleSheet("color: red;")
            frm_saldo.textsaldo.setStyleSheet("background-color: rgb(255, 255, 255); border-radius: 2px; border: 2px solid red;")

        # Verificando se há ponto ou virgula na linha de Texto Saldo
        elif saldo.count(",") or saldo.count(".") > 0:
            frm_saldo.msgerror.setText("Não insira ponto ou virgula!")
            frm_saldo.msgerror.setStyleSheet("color: red;")

        # Verificando se linha de texto não é numérica
        elif not saldo.isnumeric():
            frm_saldo.msgerror.setText("Insira apenas números!")
            frm_saldo.msgerror.setStyleSheet("color: red;")


    def transactions(self):
        # Definindo os Valores Digitados
        dados["descricao"] = frm_transacoes.textdescricao.text()
        dados["valor"] = frm_transacoes.textvalor.text()
        dados["data"] = frm_transacoes.textdata.text()

        # Colocando o valor do dados['valor'] na variálvel valor
        valor = frm_transacoes.textvalor.text()

        # Verificando se a Linha Descrição está vazia
        if frm_transacoes.textdescricao.text().strip() == "":
            frm_transacoes.textdescricao.setStyleSheet("background-color: rgb(255, 255, 255); border-radius: 2px; border: 2px solid red;")

        # Verificando se a Linha Valor está vazia
        elif frm_transacoes.textvalor.text().strip() == "":
            frm_transacoes.textvalor.setStyleSheet("background-color: rgb(255, 255, 255); border-radius: 2px; border: 2px solid red;")

        # Verificando se A ponto ou virgula na Linha Valor
        elif valor.count(',') or valor.count('.') > 0:
            frm_transacoes.lblerror.setText('Não insira ponto ou virgula!')
            frm_transacoes.lblerror.setStyleSheet('color: red;')

        # Verificando se a Linha valor é um número
        elif not valor.isnumeric():
            frm_transacoes.lblerror.setText('Insira apenas números!')
            frm_transacoes.lblerror.setStyleSheet('color: red;')

        else:
            # Fechando FormulárioTransações
            frm_transacoes.close()

            #Adicionando a Descrição no ComboBox selecionar itens do FrmRemover/Alterar Transações
            frm_remover_alterar_transacao.selecionar_item.addItem(dados["descricao"])

            # Transformando linhaValor em um número Inteiro
            valor = int(frm_transacoes.textvalor.text())

            # Adicionando variável valor no dados['valor']
            dados["valor"] = valor

            # Adicionado variável valor na lista Gastos_Saídas
            gastos_saidas.append(valor)

            # Fazendo os calculos da lblTotal_Saídas, lblTotal_Final
            frm_principal.lblsaidas.setText(lang.toString(sum(gastos_saidas) * 0.01, 'f', 2))
            frm_principal.lbltotal.setText(lang.toString((dados['saldo'] - sum(gastos_saidas)) * 0.01, 'f', 2))

            # Adicionando dados do dicionário na Lista dadoscopy
            dadoscopy.append(dados.copy())

            # Limpando as linhas de Texto
            frm_transacoes.textdescricao.clear()
            frm_transacoes.textvalor.clear()

            # Variável das linhas da tabela
            row = 0

            # Colunas serão igual ao total de dados na Lista dados copy
            frm_principal.tabela.setRowCount(len(dadoscopy))

            for dado in dadoscopy:

                # Adicionando os dados Digitados na Tabela no FrmPrincipal
                frm_principal.tabela.setItem(row, 0, QtWidgets.QTableWidgetItem(dado['descricao']))
                frm_principal.tabela.setItem(row, 1, QtWidgets.QTableWidgetItem(lang.toString(dado['valor'] * 0.01, 'f', 2)))
                frm_principal.tabela.setItem(row, 2, QtWidgets.QTableWidgetItem(dado['data']))
                row += 1


class FrmRemover_Alterar:
    def __init__(self):
        # Cliques dos Botões
        frm_remover_alterar_transacao.btn_ok.clicked.connect(FrmRemover_Alterar.ok_clicked_Alterar)
        frm_remover_alterar_transacao.btnremover.clicked.connect(FrmRemover_Alterar.remover_dados)
        frm_remover_alterar_transacao.btnalterar.clicked.connect(FrmRemover_Alterar.alterar_dados)


    def remover_dados(self):
        # Variável item armazena o texto da ComboBox
        item = frm_remover_alterar_transacao.selecionar_item.currentText()

        # Verifica se item não está vazio
        if item != '':

            # Pegando cada dado da Lista dadoscopy
            for dado in dadoscopy:

                # Verificando se item é igual ao dado
                if item == dado['descricao']:

                    # Coletando a posição do Dado
                    posicao = dadoscopy.index(dado)

                    # Removendo o dado da lista dadoscopy
                    dadoscopy.remove(dado)

                    # Removendo coluna da Tabela do FrmPrincipal
                    frm_principal.tabela.removeRow(posicao)

                    frm_principal.tabela.setRowCount(len(dadoscopy))
                    # Limpando o combobox
                    frm_remover_alterar_transacao.selecionar_item.removeItem(frm_remover_alterar_transacao.selecionar_item.currentIndex())

                    # Tirando o valor da Variavel gastos_saidas
                    gastos_saidas.remove(dado['valor'])

                    # Refazendo os calculos Total Saídas, Total Final
                    frm_principal.lbltotal.setText(lang.toString((dados['saldo'] - sum(gastos_saidas)) * 0.01, 'f', 2))
                    frm_principal.lblsaidas.setText(lang.toString(sum(gastos_saidas) * 0.01, 'f', 2))

                    # Limpando as Linhas
                    frm_remover_alterar_transacao.textdescricao.clear()
                    frm_remover_alterar_transacao.textvalor.clear()


    def alterar_dados(self):
        # Fechando FrmAlterar/Remover
        frm_remover_alterar_transacao.close()

        # Variável item é igual ao texto selecionado na ComboBox
        item = frm_remover_alterar_transacao.selecionar_item.currentText()

        # Verificando se o botão ok foi acionado, se o item é diferente de Vazio e o campo texto descricao é diferente de vazio
        if FrmRemover_Alterar.ok_clicked_Alterar and item != '' and frm_remover_alterar_transacao.textdescricao.text() != '':

            # Pegando cada dado da Lista dadoscopy
            for dado in dadoscopy:

                # Verificando se o item está nos dado['Descricao']
                if item == dado["descricao"]:
                    p = dadoscopy.index(dado)
                    # removendo valor antigo do gastos saidas
                    gastos_saidas.remove(dado['valor'])

                    # Definindo os novos dados
                    dado['descricao'] = frm_remover_alterar_transacao.textdescricao.text()
                    dado['valor'] = int(frm_remover_alterar_transacao.textvalor.text())
                    dado['data'] = frm_remover_alterar_transacao.data.text()

                    # Adicionando o novo valor
                    gastos_saidas.append(dado['valor'])

                    # Refazendo os calculos Total Saídas, Total Final
                    frm_principal.lbltotal.setText(lang.toString((dados['saldo'] - sum(gastos_saidas)) * 0.01, 'f', 2))
                    frm_principal.lblsaidas.setText(lang.toString(sum(gastos_saidas) * 0.01, 'f', 2))

                    # Limpando as linhas de Texto
                    frm_remover_alterar_transacao.textdescricao.clear()
                    frm_remover_alterar_transacao.textvalor.clear()

                    # Variável das linhas da tabela
                    row = p
                    # Colunas serão igual ao total de dados na Lista dados copy
                    frm_principal.tabela.setRowCount(len(dadoscopy))

                    # Adicionando os dados Digitados na Tabela no FrmPrincipal
                    frm_principal.tabela.setItem(row, 0, QtWidgets.QTableWidgetItem(dado['descricao']))
                    frm_principal.tabela.setItem(row, 1, QtWidgets.QTableWidgetItem(lang.toString(dado['valor'] * 0.01, 'f', 2)))
                    frm_principal.tabela.setItem(row, 2, QtWidgets.QTableWidgetItem(dado['data']))
                    row += 1

                    # Removendo o antigo texto da combobox
                    frm_remover_alterar_transacao.selecionar_item.removeItem(frm_remover_alterar_transacao.selecionar_item.currentIndex())

                    # Adicionando o novo texto na combobox
                    frm_remover_alterar_transacao.selecionar_item.addItem(dado['descricao'])


    def ok_clicked_Alterar(self):
        # Variável item é igual ao texto selecionado na ComboBox
        item = frm_remover_alterar_transacao.selecionar_item.currentText()

        # Pegando cada dado da Lista dadoscopy
        for dado in dadoscopy:

            # Verificando se o item está nos dado['Descricao']
            if item in dado["descricao"]:

                # colocando os dados nas Linhas de Textos
                frm_remover_alterar_transacao.textdescricao.setText(dado['descricao'])
                frm_remover_alterar_transacao.textvalor.setText(str(dado['valor']))


if __name__ == '__main__':
    # Variáveis,Listas e Dicionário
    dados = {}
    data_atual = date.today()
    dadoscopy = []
    loc = QtCore.QLocale.system().name()
    lang = QtCore.QLocale(loc)
    gastos_saidas = []

    # Configurando Aplicação
    app = QtWidgets.QApplication([])
    frm_principal = uic.loadUi("View/frm_principal.ui")
    frm_saldo = uic.loadUi("View/frm_saldo.ui")
    frm_transacoes = uic.loadUi("View/frm_transacoes.ui")
    frm_remover_alterar_transacao = uic.loadUi("View/frm_remover_alterar_transaçoes.ui")

    # Exibindo FrmPrincipal
    FrmPrincial()


    # inicialiando Aplicação
    app.exec()
