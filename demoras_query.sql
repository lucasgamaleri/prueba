SELECT produccion.Bobina, produccion.[Fecha Produccion], produccion.[Grupo Calidad], produccion.[Grupo Ancho], produccion.[Grupo Espesor], produccion.Ancho, produccion.[Material Refilado], produccion.[Cambio Ancho No Refilado], demoras.Subconcepto FROM produccion INNER JOIN demoras ON produccion.Bobina = demoras.Bobina WHERE (((produccion.[Fecha Produccion])>#7/30/2019 6:0:0# And (produccion.[Fecha Produccion])<#7/31/2019 6:0:0#));