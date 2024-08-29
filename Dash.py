from dash import Dash, html, dcc, Input, Output # Dcc = componentes do dashboard
import plotly.express as px # Criar gráficos
import pandas as pd

app = Dash(__name__) # Inicialização do App
 
df = pd.read_excel("Dashboard/Vendas.xlsx")

# Criando o Gráafico
fig = px.bar(df, x="Produto", y="Quantidade", color="ID Loja", barmode="group")
opcoes = list(df['ID Loja'].unique())
opcoes.append("Todas as Lojas")

app.layout = html.Div(children=[
    html.H1(children='Faturamento das Lojas'),
    html.H2(children='Gráfico contendo todos os produtos separados por loja'),

    html.Div(children='''
        OBS: Esse gráfico mostra a quantidade de produtos vendidos, não o faturamento.
    '''),   

    dcc.Dropdown(opcoes, value='Todas as Lojas', id='Lista_Lojas'),  

    dcc.Graph(
        id='grafico_quantidade_vendas',
        figure=fig
    )
])

@app.callback( # Decorator 
    Output('grafico_quantidade_vendas', 'figure'), # quem eu quero/vai ser modificado
    Input('Lista_Lojas', 'value') # quem é que ta trazendo a informação
)
def update_output(value): # Conecta o Input e Output
    if value == "Todas as Lojas":
        fig= px.bar(df, x="Produto", y="Quantidade", color="ID Loja", barmode="group")
    else:
        tabela_filtrada = df.loc[df['ID Loja']==value, :] # ":" = Todas 
        fig= px.bar(tabela_filtrada, x="Produto", y="Quantidade", color="ID Loja", barmode="group")
    return fig

if __name__ == '__main__': # Coloca online o site(gráfico)
    app.run(debug=True)
