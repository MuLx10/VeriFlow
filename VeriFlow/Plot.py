import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

def MapNames(names):
	if type(names) is list:
		return [x.split('.')[-1] for x in names]
	return names.split('.')[-1]

def PlotTopology(network):
	W = network.switches
	H = network.hosts

	# start, end = [], []
	grp = {}

	G=nx.Graph()

	for w in W.values():
		grp[w.getId()] = 'Switch'
		for nh in w.getNextHops():
			G.add_edge(MapNames(w.getId()), MapNames(nh))
			# start.append(w.getId())
			# end.append(nh)
		for h in w.getConnectedHosts():
			grp[h] = 'Host'
			G.add_edge(MapNames(w.getId()), MapNames(h))
			# start.append(w.getId())
			# end.append(h)

	# start, end = MapNames(start), MapNames(end)

	# df = pd.DataFrame({ 'from':start, 'to':end})
	# G = nx.from_pandas_edgelist(df, 'from', 'to')

	carac = pd.DataFrame({ 'ID': MapNames(list(grp.keys())), 'node_color': list(grp.values())})
	carac= carac.set_index('ID')

	carac=carac.reindex(G.nodes())
	carac['node_color']=pd.Categorical(carac['node_color'])


	unique = np.unique(carac['node_color'].cat.codes)
	switch = mpatches.Patch(color='r', label='Switch')
	host = mpatches.Patch(color='g', label='Host')
	plt.legend(handles=[switch, host])
	colors = ['r' if x==1 else 'g' for x in carac['node_color'].cat.codes]

	nx.draw(G, with_labels=True, node_size=100, node_color=colors, node_shape="o", alpha=0.9, linewidths=20)
	# plt.legend(unique)
	plt.show()

