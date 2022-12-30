from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc

# buat dash app 
app = Dash(external_stylesheets=[dbc.themes.LUX])

# buat judul dsahboard
app.title = 'Employee Attrition & Performance'

# komponen dashboard 

## 1.buat navbar
navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink(" ", href="#")),
    ],
    brand="Employee Attrition & Performance",
    brand_href="#",
    color="#006400",
    dark=True,
)

## 2.load data set
# read data
attrition = pd.read_csv('WA_Fn-UseC_-HR-Employee-Attrition.csv')
attrition.head()

# replace kolom Education
attrition['Education'] = attrition['Education'].replace(1, 'Below College')
attrition['Education'] = attrition['Education'].replace(2, 'College')
attrition['Education'] = attrition['Education'].replace(3, 'Bachelor')
attrition['Education'] = attrition['Education'].replace(4, 'Master')
attrition['Education'] = attrition['Education'].replace(5, 'Doctor')

# replace kolom EnvironmentSatisfaction
attrition['EnvironmentSatisfaction'] = attrition['EnvironmentSatisfaction'].replace(1 , 'Low')
attrition['EnvironmentSatisfaction'] = attrition['EnvironmentSatisfaction'].replace(2 , 'Medium')
attrition['EnvironmentSatisfaction'] = attrition['EnvironmentSatisfaction'].replace(3 , 'High')
attrition['EnvironmentSatisfaction'] = attrition['EnvironmentSatisfaction'].replace(4 , 'Very High')

# replace kolom JobInvolvement
attrition['JobInvolvement'] = attrition['JobInvolvement'].replace(1 , 'Low')
attrition['JobInvolvement'] = attrition['JobInvolvement'].replace(2 , 'Medium')
attrition['JobInvolvement'] = attrition['JobInvolvement'].replace(3 , 'High')
attrition['JobInvolvement'] = attrition['JobInvolvement'].replace(4 , 'Very High')

# replace kolom JobSatisfaction
attrition['JobSatisfaction'] = attrition['JobSatisfaction'].replace(1 , 'Low')
attrition['JobSatisfaction'] = attrition['JobSatisfaction'].replace(2 , 'Medium')
attrition['JobSatisfaction'] = attrition['JobSatisfaction'].replace(3 , 'High')
attrition['JobSatisfaction'] = attrition['JobSatisfaction'].replace(4 , 'Very High')

# replace kolom PerformanceRating
attrition['PerformanceRating'] = attrition['PerformanceRating'].replace(1 , 'Low')
attrition['PerformanceRating'] = attrition['PerformanceRating'].replace(2 , 'Good')
attrition['PerformanceRating'] = attrition['PerformanceRating'].replace(3 , 'Excellent')
attrition['PerformanceRating'] = attrition['PerformanceRating'].replace(4 , 'Outstanding')

# replace kolom RelationshipSatisfaction
attrition['RelationshipSatisfaction'] = attrition['RelationshipSatisfaction'].replace(1 , 'Low')
attrition['RelationshipSatisfaction'] = attrition['RelationshipSatisfaction'].replace(2 , 'Medium')
attrition['RelationshipSatisfaction'] = attrition['RelationshipSatisfaction'].replace(3 , 'High')
attrition['RelationshipSatisfaction'] = attrition['RelationshipSatisfaction'].replace(4 , 'Very High')

# replace kolom WorkLifeBalance
attrition['WorkLifeBalance'] = attrition['WorkLifeBalance'].replace(1 , 'Bad')
attrition['WorkLifeBalance'] = attrition['WorkLifeBalance'].replace(2 , 'Good')
attrition['WorkLifeBalance'] = attrition['WorkLifeBalance'].replace(3 , 'Better')
attrition['WorkLifeBalance'] = attrition['WorkLifeBalance'].replace(4 , 'Best')

# sesuaikan tipe data
attrition['Attrition'] = attrition['Attrition'].astype('category')
attrition['BusinessTravel'] = attrition['BusinessTravel'].astype('category')
attrition['Department'] = attrition['Department'].astype('category')
attrition['Education'] = attrition['Education'].astype('category')
attrition['EducationField'] = attrition['EducationField'].astype('category')
attrition['EnvironmentSatisfaction'] = attrition['EnvironmentSatisfaction'].astype('category')
attrition['Gender'] = attrition['Gender'].astype('category')
attrition['JobInvolvement'] = attrition['JobInvolvement'].astype('category')
attrition['JobRole'] = attrition['JobRole'].astype('category')
attrition['JobSatisfaction'] = attrition['JobSatisfaction'].astype('category')
attrition['MaritalStatus'] = attrition['MaritalStatus'].astype('category')
attrition['OverTime'] = attrition['OverTime'].astype('category')
attrition['PerformanceRating'] = attrition['PerformanceRating'].astype('category')
attrition['RelationshipSatisfaction'] = attrition['RelationshipSatisfaction'].astype('category')
attrition['WorkLifeBalance'] = attrition['WorkLifeBalance'].astype('category')


## 3.buat card content
# card content 1
information_card = [
    dbc.CardHeader('Information'),
    dbc.CardBody([
        html.P('This is the information of employeed in IBM. Help to analyst Employee Attrition & Performance'),
    ])
]

# card content 2
employee_card = [
    dbc.CardHeader('Total Employee'),
    dbc.CardBody([
        html.H1(attrition.shape[0])
    ]),
]

# card content 3
attrition_yes = [
    dbc.CardHeader('Attrition Yes'),
    dbc.CardBody([
        html.H1(attrition[attrition['Attrition'] == 'Yes'].shape[0], style={'color':'red'})
    ]),
]

# card content 4
attrition_no = [
    dbc.CardHeader('Attrition No'),
    dbc.CardBody([
        html.H1(attrition[attrition['Attrition'] == 'No'].shape[0], style={'color':'navy'})
    ]),
]

### tampilkan bar_plot1
attrition_agg = attrition.groupby(['Department','Attrition']).count()[['EmployeeNumber']].reset_index()
bar_plot1 = px.bar(
    attrition_agg.sort_values('EmployeeNumber'),
       x='EmployeeNumber',
       y='Department',
       color='Attrition',
       orientation='h',
       barmode = 'group',
       template = 'ggplot2',
       labels = {
        'Department': 'Department',
        'EmployeeNumber': 'Employee Number',
        'Attrition': 'Attrition',
    },
    title = 'Employee Number in Each Department',
    height=700,
).update_layout(showlegend=False)


### tampilkan line_plot2
# buat kolom baru dengan lama tahun awal masuk kerja
attrition['Tahun_Masuk'] = 2022 - attrition['TotalWorkingYears']
year_2010 = attrition[attrition['Tahun_Masuk'] >= 2010]
year_2010_agg = year_2010.groupby(['Tahun_Masuk']).count()[['EmployeeNumber']].reset_index()
year_2010_agg

line_plot2 = px.line(
    year_2010_agg,
    x = 'Tahun_Masuk',
    y = 'EmployeeNumber',
    markers=True,
    color_discrete_sequence = ['#618685'],
    template = 'ggplot2',
    labels={
        'Tahun_Masuk':'Tahun Masuk',
        'EmployeeNumber':'Employee Number'
    },
    title = 'Number of new hires in the last 30 days',
    height=700,
    )


# User Interface
app.layout = html.Div([
    navbar,
    html.Br(),

    #### ----ROW1----
    dbc.Row([

        ## Row 1 Col 1
        dbc.Col(dbc.Card(information_card, color='#00FFFF'), width=6),

        ## Row 1 Col 2
        dbc.Col(dbc.Card(employee_card, color='#d64161'), width=2),

        ## Row 1 Col 3
        dbc.Col(dbc.Card(attrition_yes, color='#feb236'), width=2),

        ## Row 1 Col 4
        dbc.Col(dbc.Card(attrition_no, color='#6b5b95'), width=2),

    ]),

    html.Br(),

    ### ----ROW2----
    dbc.Row([

        ## Row 2 Col 1
        dbc.Col(dbc.Tabs([
            # Tab 1
            dbc.Tab(dcc.Graph(figure=bar_plot1),
            label='Each Department'),

            # Tab 2
            dbc.Tab(dcc.Graph(figure=line_plot2),
            label='Tahun Masuk Pekerja'),
        ])),

        ## Row 2 Col 2
        dbc.Col([
            dcc.Dropdown(
                id='choose_dept',
                options=attrition['Department'].unique(),
                value='Research & Development',
            ),
            dcc.Graph(id='plot3'),
        ]),

    ]),
])

@app.callback(
    Output(component_id='plot3', component_property='figure'),
    Input(component_id='choose_dept', component_property='value')
)

def update_plot(dept_name):
    data_agg = attrition[attrition['Department'] == dept_name]
    hist_plot3 = px.histogram(
        data_agg,
        x = 'MonthlyIncome',
        nbins = 20,
        color_discrete_sequence = ['#618685','#80ced6'],
        title = f'Monthly Income in {dept_name} Department',
        template = 'ggplot2',
        labels={
            'MonthlyIncome': 'Monthly Income',
        },
        marginal = 'box',
        height=700,
    )
    return hist_plot3

# Run app at local
if __name__ == '__main__':
    app.run_server(debug=True)