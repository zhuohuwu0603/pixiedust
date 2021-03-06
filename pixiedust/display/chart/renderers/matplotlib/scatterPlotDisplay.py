# -------------------------------------------------------------------------------
# Copyright IBM Corp. 2017
# 
# Licensed under the Apache License, Version 2.0 (the 'License');
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
# http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an 'AS IS' BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# -------------------------------------------------------------------------------

from pixiedust.display.chart.renderers import PixiedustRenderer
from .matplotlibBaseDisplay import MatplotlibBaseDisplay
import matplotlib.pyplot as plt
import mpld3
import numpy as np

@PixiedustRenderer(id="scatterPlot")
class ScatterPlotDisplay(MatplotlibBaseDisplay):
    
	def supportsAggregation(self, handlerId):
		return False

	def supportsLegend(self, handlerId):
		return False

	def supportsKeyFields(self, handlerId):
		return False
    
	def canRenderChart(self):
		valueFields = self.getValueFields()
		if len(valueFields) < 2:
			return (False, "At least two numerical columns required.")
		else:
			return (True, None)

	def getPreferredDefaultValueFieldCount(self, handlerId):
		return 2

	def matplotlibRender(self, fig, ax):
		valueFieldValues = self.getValueFieldValueLists()
		valueFields = self.getValueFields()
		paths = ax.scatter(valueFieldValues[0],valueFieldValues[1],c=valueFieldValues[1],marker='o',alpha=0.7,s=124,cmap=self.colormap)
		labels = []
		for i in range(len(valueFieldValues[0])):
			labels.append('({0},{1})'.format(valueFieldValues[0][i],valueFieldValues[1][i]))
		if self.has_mpld3:
			tooltip = mpld3.plugins.PointLabelTooltip(paths, labels=labels)
			mpld3.plugins.connect(fig, tooltip)
		ax.set_xlabel(valueFields[0], size=14)
		ax.set_ylabel(valueFields[1], size=14)