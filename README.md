# ChemInfo
This code provides a gui interface that allows the user to find chemical properties from pubchem.
In the main window, the user needs to give an input that must be the chemical formula of a compound. Next they had to press the submit
button. This button verifies if the compound exists. If it exists a secondary window will open, and if it doesn't a warning message
will be shown informing that the input it's wrong, and the user needs to try again.
The secondary window, will show in the title the chemical formula of the compound put in the input. Also, will show eleven buttons, 10
of them are properties (Cid, Molecular weight, Iupac name, Synonym, Elements, Isomeric smiles, Exact Mass, Hidrogen bond donor count,
Hidrogen bond acceptor count and Complexity). If the user decides press any of these buttons a messagebox it will be open with that
information. In the other hand, the eleven button creates a .txt file that will have the ten properties of the other buttons. The name 
of this file will be 'Information about your compound'.
