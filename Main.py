
from VeriFlow.Network import Network

ROUTE_VIEW = 1;
BIT_BUCKET = 2;


def main():
	print("Enter network configuration file name (eg.: file.txt):");
	# filename = input("> ");
	filename = "Topo1.txt"
	network = Network();
	network.parseNetworkFromFile(filename);
	generatedECs = network.getECsFromTrie();
	network.checkWellformedness();
	network.log(generatedECs);
	while True:
		print(" ");
		print("Add rule by entering A#switchIP-rulePrefix-nextHopIP (eg.A#127.0.0.1-128.0.0.0/2-127.0.0.2)");
		print("Remove rule by entering R#switchIP-rulePrefix-nextHopIP (eg.R#127.0.0.1-128.0.0.0/2-127.0.0.2)");
		print("To exit type exit");

		affectedEcs = set()
		inputline = input('> ')
		if (inputline.startswith("A")):
			affectedEcs = network.addRuleFromString(inputline[2:]);
			network.checkWellformedness(affectedEcs);
		elif (inputline.startswith("R")):
			affectedEcs = network.deleteRuleFromString(inputline[2:]);
			network.checkWellformedness(affectedEcs);
		elif ("exit" in inputline):
			break;
		else:
			print("Wrong input format!");
			continue;

		print("");
		network.log(affectedEcs);

if __name__ == '__main__':
	main()