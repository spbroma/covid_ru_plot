import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from get_data import get_data
from datetime import datetime

align_value = 20
data = get_data(align_value)
print('Data is loaded')

dateArr = data.date
valArr = data.value
valArrAlign = data.value_align
labelAnnotationArr = data.annotation
labelAnnotationAllArr = data.annotation_all
labelArr = data.label
doubleEveryN = data.double_plot.value
doubleEveryNLabel = data.double_plot.label
maxLenValArrAlign = data.max_len
newCasesAlignArr = data.new_cases_align
newCasesArr = data.new_cases


# Base plotly

fig = go.Figure()

datestr = datetime.strftime(datetime.now(), '%d.%m.%Y, %H:%M')

# for i in range(len(doubleEveryN)):
#     fig.add_trace(go.Scatter(y=doubleEveryN[i],
#                              name=doubleEveryNLabel[i],
#                              hovertemplate=doubleEveryNLabel[i],
#                              # text=doubleEveryNLabel[i],
#                              mode='lines',
#                              line=dict(
#                                  color='#888888',
#                                  width=1,
#                                  dash='dash'
#                              )
#                              )
#                   )
#
# def click_handler(trace, points, selector):
#     print(trace)

dateArrShort = []
for d in dateArr:
    dateArrShort.append(d[:-3])
dateArrShort = np.array(dateArrShort)

# Relative value
n_first = 10
colors = px.colors.qualitative.G10
for i in range(valArrAlign.shape[0]):
    if i < n_first:
        visible = None
    else:
        visible = 'legendonly'

    s = go.Scatter(y=newCasesArr[i],
                   x=dateArr,
                    mode='lines+markers+text',
                    name=labelArr[i],
                    text=labelAnnotationAllArr[i],
                    textposition="middle right",
                    # hovertext=str(valArrAlign[i]) + ', ' + labelArr[i],
                    hovertemplate='%{y}, ' + labelArr[i],
                    marker=dict(color=colors[i%len(colors)], size=7),
                    line=dict(color=colors[i%len(colors)], width=2),
                    visible=visible,
                    # showlegend=False
                             )

    # s.on_click(click_handler)
    fig.add_trace(s)



# Absolute value
# for i in range(dateArr.shape[0]):
#     fig.add_trace(go.Scatter(y=valArr[i, :], x=dateArr,
#                     mode='lines+markers',
#                     name=labelArr[i]))

fig.update_yaxes(type="linear", title_text='Число новых случаев')
# fig.update_xaxes(title_text='Количество дней с момента регистрации ' + str(align_value) + ' заболевших')

fig.update_layout(title='График новых случаев COVID-19 по регионам РФ на ' + dateArr[-1])

# fig.add_annotation(
#             x=10,
#             y=1000,
#             text="dict Text 2")


fig.update_layout(

    # clickmode='event+select',
    # margin=dict(l=20, r=20, t=20, b=20),

    # width=1500,
    # height=700,
    xaxis=dict(
        range=[0, np.ceil((newCasesArr.shape[1]+3)/5)*5],
        # fixedrange=True
    ),

    # yaxis=dict(
    #     range=[np.log10(align_value), np.log10(valArr.max()) * 1.1],
    #     # fixedrange=True
    # ),

    updatemenus=[
        dict(
            type="buttons",
            direction="left",
            buttons=list([
                dict(
                    args=["yaxis.type", "log"],
                    label="логарифмический",
                    method="relayout"
                ),
                dict(
                    args=["yaxis.type", "linear"],
                    label="линейный",
                    method="relayout"
                ),
            ]),
            pad={"r": 10, "t": 10},
            showactive=True,
            x=0.005,
            xanchor="left",
            y=1.09,
            yanchor="top"
        ),

        dict(
            type = "buttons",
            direction = "left",
            buttons=list([
                dict(
                    args=["mode", "lines+markers+text"],
                    label="Подписи",
                    method="restyle"
                ),
                dict(
                    args=["mode", "lines"],
                    label="Без подписей",
                    method="restyle"
                ),
            ]),
            pad={"r": 10, "t": 10},
            showactive=True,
            x=1.005,
            xanchor="right",
            y=1.09,
            yanchor="top"
        ),
    ]
)

print('Plotting done')

fig.write_html('covid_new.html', auto_open=True)

# Plotly Express

# dateArr = dateArr.reshape([1, len(dateArr)])
# labelArr = np.insert(labelArr, 0, 'date')
#
# dateValArr = np.concatenate((dateArr, valArr)).transpose()
#
# df = pd.DataFrame(dateValArr, columns=labelArr)
#
# dfLong = df.melt('date')
#
# fig = px.line(dfLong, x='date', y='value', color="variable", log_y=True)
# fig.write_html('index.html', auto_open=True)



# df = px.data.gapminder().query("continent=='Oceania'")
# fig = px.line(df, x="year", y="lifeExp", color='country')
# # fig.show()
# fig.write_html('first_figure.html', auto_open=True)

# import plotly.graph_objects as go
# fig = go.Figure(data=go.Bar(y=[2, 3, 1]))
# fig.write_html('first_figure.html', auto_open=True)