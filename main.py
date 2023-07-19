import pandas as pd
from data.platosRestaurante import platosPopulares
from helpers2.lanzarTabla import lanzarTablaHTML
tablaPlatos= pd.DataFrame(platosPopulares)
lanzarTablaHTML(tablaPlatos,"tabla1")