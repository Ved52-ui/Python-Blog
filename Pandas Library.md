<h1>--How To Import Pandas Library</h1><br>
<h2>--To Install Pandas Library Use This Code </h2><br>

      pip install pandas
<h2>--To Import Pandas Library Use This Code </h2><br>

      import pandas as pd

<h2>--How To Make Raw And Column Using pandas</h2><br>

    data={
    "name":["ved","patel"]
    "age":[17,20]
    }
    df=pd.DataFrame(data)
    print(df)

<h1>--!!This Code Must Be Run In Jupyter Notebook!!</h1><br>
<h1>--How To Create Data Frame Using Pandas<br></h1><br>

      #creating data frame
      data={
          "Name":["Kane","Khan","Lion","Tiger"],
          "Gender":["Female","Male","Male","Male"],
          "Town":["Hemilton","Cricthurch","Bengaluru","Sydney"]
      }

      df=pd.DataFrame(data)
      print(df)
<h1>--How To Convert Data Frame Into CSV File<br></h1><br>

      df.to_csv("Your_csv_file.csv",index=False)
      df3=pd.read_csv('my_data_frame.csv')
      print(df3)
<h2>-When you print data then data was converted into csv file</h2><br>
<h1>--How To Read Many Type Of File Using Pandas</h1>
<p>----Types Of Files We Can Read Using Pandas</p><br>
<table>
<tr>
<tr><td>CSV File<br> </td></tr>
<tr><td>Excel File<br> </td></tr>
<tr><td> Json File<br> </td></tr>
<tr><td> PDF File<br> </td></tr>

</tr>
</table>
<p>----Code To Read Files For Each Type</p>

      df1=pd.read_csv('Automobile.csv')
      df1=pd.read_excel('Your_file.xlsx')
      df1=pd.read_json('Your_file.json')
      df1=pd.read_pdf(r'Your_file.pdf')
<h1>--How To Connect SQL Database Using Pandas<br></h1>
<p>----ode To Connect SQL Database</p>
                  
      #import sqlite3
      #conn=sqlite3.connect(r'your_database.db')
      #df=pd.read_sql_query(SELECT*FROM conn)
