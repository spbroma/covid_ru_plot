import numpy as np
import pandas as pd
from datetime import datetime
from munch import Munch
from load_csv import load_csv


def get_data(align_value=20):

    load_csv()
    dfIn = pd.read_csv('data.csv')
    dfDensity = pd.read_csv('data/density.csv')
    dfIn = dfIn.sort_values(by=dfIn.columns[-1], ascending=False, ignore_index=True)
    # dfIn = pd.read_csv('covid_data.csv')

    dateArr = []

    for i in range(dfIn.shape[1]-4):
        dateIn = dfIn.axes[1][i+4]
        dateOut = datetime.strptime(dateIn, '%m/%d/%y').strftime('%d %b')
        dateArr.append(dateOut)
        # print(dateOut)


    valArr = []
    valArrAlign = []
    labelArr = []
    maxLenValArrAlign = 0
    labelAnnotationArr = []
    labelAnnotationAllArr = []

    for i in range(dfIn.shape[0]-4):
        val = dfIn.loc[i][4:].to_list()
        label = dfIn.loc[i][1]
        valArr.append(val)
        labelArr.append(label)

        valAlign = []

        for v in val:
            if v >= align_value:
                valAlign.append(v)
        if len(valAlign) > maxLenValArrAlign:
            maxLenValArrAlign = len(valAlign)

        labelAnnotation = ['']*len(valAlign)
        labelAnnotationAll = ['']*len(val)

        if len(valAlign) > 0:
            labelAnnotation[-1] = label

        labelAnnotationAll[-1] = label

        valArrAlign.append(valAlign)
        labelAnnotationArr.append(labelAnnotation)
        labelAnnotationAllArr.append(labelAnnotationAll)

    doubleEvery1 = []
    doubleEvery2 = []
    doubleEvery3 = []
    doubleEvery5 = []
    doubleEvery10 = []
    # z = 10.^(x*log10(2)/3 + 1)
    for i in range(maxLenValArrAlign*2):
        doubleEvery1.append(align_value**(i * np.log10(2) / 1 + 1))
        doubleEvery2.append(align_value**(i * np.log10(2) / 2 + 1))
        doubleEvery3.append(align_value**(i * np.log10(2) / 3 + 1))
        doubleEvery5.append(align_value**(i * np.log10(2) / 5 + 1))
        doubleEvery10.append(align_value**(i * np.log10(2) / 10 + 1))


    doubleEveryN = [doubleEvery1, doubleEvery2, doubleEvery3, doubleEvery5, doubleEvery10]
    doubleEveryNLabel = ['Удвоение случаев каждый день',
                         'Удвоение случаев каждые 2 дня',
                         'Удвоение случаев каждые 3 дня',
                         'Удвоение случаев каждые 5 дней',
                         'Удвоение случаев каждые 10 дней',
                         ]

    # labelArr = clearLabels(labelArr)

    dateArr = np.array(dateArr)
    valArr = np.array(valArr)
    valArrAlign = np.array(valArrAlign)
    labelArr = np.array(labelArr)

    output = Munch()
    output.date = dateArr
    output.value = valArr
    output.value_align = valArrAlign
    output.annotation = labelAnnotationArr
    output.annotation_all = labelAnnotationAllArr
    output.label = labelArr
    output.double_plot = Munch()
    output.double_plot.value = doubleEveryN
    output.double_plot.label = doubleEveryNLabel
    output.max_len = maxLenValArrAlign

    # output1 = dict(
    #     date=dateArr,
    #     value=valArr,
    #     value_align=valArrAlign,
    #     labels=labelArr,
    #     annotations=labelAnnotationArr,
    #     double_every=dict(
    #         data=doubleEveryN,
    #         label=doubleEveryNLabel,
    #     ),
    # )

    return output


if __name__ == '__main__':
    data = get_data()