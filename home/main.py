#CONFIG
TITLE='Server Dashboard'
TIME_STEP=0.1

from nicegui import ui

# Definition: parameter, function, class
IP="10.11.5.66"
ports={80:"Jupyter Lab: beat syncamore",
       8080:"server dashboard (this page)",
       4000:"JupyterLab: quantum machine learning",
       4001:"JupyterLab: NN decoder, pytorch",       
    }
def get_link(IP,p):
    link = "http://"+IP+":"+str(p)
    return ui.link(link,link)

  
#layout
ui.label(TITLE)

ui.label("""
Author: Weilei Zeng
Date: Jun 19, 2023
""")

rows = [ {'item' : ports[p],
          'port':p,
          'link':"http://"+IP+":"+str(p) } for p in ports]




def my_table(row):
    with ui.element('div').classes('columns-6 w-full gap-2'):
        height=50
        tailwind = f'mb-2 p-2 h-[{height}px] bg-blue-100 break-inside-avoid'
        with ui.card().classes(tailwind):            
            ui.label(row['item'])
        with ui.card().classes(tailwind):                        
            ui.label(row['port'])
        with ui.card().classes(tailwind):                        
            ui.link(row['link'],row['link'])

for row in rows:
    my_table(row)



ui.textarea(label='Temp Log:', placeholder='log:')


ui.run(title=TITLE)
