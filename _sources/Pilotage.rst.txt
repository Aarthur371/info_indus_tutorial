*********
Pilotage des moteurs
*********

Afin de piloter les moteurs dynamixels, il est recommandé de suivre cette vidéo : 

`Quick start guide for Rasberry Pi <https://www.youtube.com/watch?time_continue=2&v=-MafNIZUCHA&embeds_referring_euri=https%3A%2F%2Femanual.robotis.com%2F&source_ve_path=Mjg2NjY>`_

.. https://emanual.robotis.com/docs/en/dxl/dxl-quick-start-guide/ (suivre la vidéo)

.. note::
   Attention : opération de clonage à faire avec ROS_DISTRO = humble

.. code-block:: bash
   Git clone -b humble-devel --depth 1 https://github.com/ROBOTIS-GIT/DynamixelSDK

.. note::
   Argument --depth 1 : permet de prendre que la dernière version pour gagner de la place (évite aussi les erreurs)


Ajouter les addon du tuto yguel au bashrc pour debugger plus facilement !
Puis reprendre tuto video (ajout utilisateur à ,un groupe avec usermod, etc)

Read write node error : ouvirir le fichier correspondant
Chercher control table dans la doc dxl/ax sur emanual robotis
Régler paramètres torque enable, baud rate, version protocol 1.0
Recompiler : ros2_build