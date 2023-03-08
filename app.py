from flask import Flask, request
from flask import render_template
import pandas as pd

popular_df = pd.read_csv('populardf.csv')
donation = pd.read_csv('dona.csv')
sort_df = pd.read_csv('sort_df.csv')

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html',
                           pincode=list(popular_df['Pincode'].values),
                           area=list(popular_df['Area'].values),
                           poverty_rate=list(popular_df['Poverty_Rate'].values),
                           city=list(popular_df['City'].values)
                           )


@app.route('/Recomend')
def recommend_ui():
    return render_template('Recomend.html')


@app.route('/recomend_area', methods=['post'])
def recomend():
    inp1 = request.form.get('user_input1')
    inp = request.form.get('user_input2')

    # inp1 = input("Enter the City Name: ")
    # inp = input("Enter Area Name: ")
    length = len(donation)
    data = []
    for i in range(0, length):
        if sort_df['Area'].loc[i] == inp:
            if sort_df['Poverty-Rate'].loc[i] >= 0.10:
                #         str1 = inp
                #                 print("You can Donate")
                str1 = 'You can Donate in this Area'
                return render_template('Recomend.html', str1=str1)
                break
            else:
                print('Recommendations for {0}:\n'.format(inp))
                #                 print('{0}'.format(sort_df[sort_df['City'] == inp1].head(5)))
                sidf = sort_df[sort_df['City'] == inp1].head(5)
                data.extend(sidf.values.tolist())
                print(data)
                return render_template('Recomend.html', data=data)
                break

    # return user_input1,user_input2


if __name__ == '__main__':
    app.run(debug=True)
