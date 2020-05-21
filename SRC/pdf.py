import pandas as pd
import numpy as np
import re
from fpdf import FPDF
import requests
import matplotlib.pyplot as plt
from df_to_image import to_png

def genPDF(df_lista):
    
    pdf = FPDF('P','mm','A4') #210 x 297 mm vertical

    #Page
    pdf.add_page()

    #Nasdaq image superior
    pdf.image("imagen.png",10,10, 65,20)

    # parameters
    w,h=190,277
    font_type = ('Arial', 'B', 15)
    pdf.set_font(*font_type)
    pdf.set_text_color(0)
    pdf.set_draw_color(0)

    # Title
    pdf.set_xy(8,50)
    pdf.cell(25,80)
    pdf.cell(150,10,f"Esta es tu lista de la compra",0,1,"C")  

    # Data
    pdf.set_fill_color(121, 181, 161)
    font_type = ('Arial', '', 12)
    pdf.set_font(*font_type)


    #Adding body
    to_png(df_lista)
    pdf.image("body.png",15,5, 180,180)


    #company plot
    # stats_pdf(company)

    #Adding plot
    # pdf.image("evolucion.png",30,140, 140,95)


    #Output
    pdf.output("LaComprApp-PDF.pdf","F")

         