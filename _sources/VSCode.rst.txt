*********
VSCode
*********

Cette partie decrit comment installer Vscode sur Rasberry Pi.

=====================
Preparer le Rasberry Pi
=====================
Avant d'installer Vscode, il est necessaire de mettre a jour la Rasberry Pi.

.. code-block:: bash
   
   sudo apt-get update
   sudo apt-get upgrade

Installer les dependances necessaires pour VSCode:

.. code-block:: bash
   
   sudo apt-get install -y libx11-dev libxkbfile-dev libsecret-1-dev

====================
Telecharger et Installer VSCode
====================
Telecharger le paquet .deb pour ARM depuis le site officiel de VSCode:

.. code-block:: bash
   
   wget https://code.visualstudio.com/sha/download?build=stable&os=linux-deb-arm

Renommer le fichier telecharge:

.. code-block:: bash
   
   mv download?build=stable&os=linux-deb-arm vscode-arm.deb

Installer le paquet .deb:

.. code-block:: bash
   
   sudo dpkg -i vscode-arm.deb

Corriger les eventuelles erreurs de dependances:

.. code-block:: bash
   
   sudo apt --fix-broken install


=====================
Lancer et Configurer VSCode
=====================
Lancer VSCode:

.. code-block:: bash
   
   code

Configurer l'editeur selon vos preferences, en installant des extensions utiles. Par exemple, pour le developpement Python, vous pouvez installer l'extension Python pour VSCode:

.. code-block:: bash
   
   code --install-extension ms-python.python


===================
Mettre à jour VSCode
===================

Vérifier la présence de mises à jour disponibles pour VSCode:

.. code-block:: bash
   
   sudo apt update 
   sudo apt upgrade code