# enPiT Summer School 2022

## How to use

1. Clone this repository. (e.g. `cd ~/catkin_ws/src && git clone https://github.com/GNagahashi/enpit2022_summer.git`)
2. Rename this repository in the local from `enpit2022_summer` to `gnc`. (e.g. `mv enpit2022_summer/ gnc`)
3. Build on BridgePoint.
4. Run in Terminal. (Need `iq_sim` and `iq_gnc` packages)
```sh
cd ~/Desktop
./simulator.sh
# New tab, after 'cd ~/Desktop'
./sitl.sh
# New window, after 'source ~/.bashrc && source <your work space>/devel/setup.bash'
roscore
# New tab
roslaunch iq_sim apm.launch
# New tab
rosrun gnc ctrl
```

  
-----
  

# gnc: An example project of BridgePoint for controlling quad copter for APRIS Robot Challange

## How to run

1. Use hisazumi/aprisrc-sitl docker image

* https://hub.docker.com/repository/docker/hisazumi/aprisrc-sitl
* https://github.com/hisazumi/aprisrc-sitl

2. Download this project in catkin_ws/src in the conatiner
```
cd ~/catkin_ws/src
git clone https://github.com/hisazumi/gnc.git
```

3. Import to your bridgepoint workspace

* launch bridgepoint (just type 'bridgepoint' on termianl in the container)
* File menu -> Import -> General/Existing Project into Workspace -> Select root directory
* and select imported directory (it should be ~/catkin_ws/src/gnc)
* Build on BridgePoint (Ctrl+B or Project menu -> Build all)

4. Run in terminal

* Before executing gnc, run simulator.sh, sitl.sh, and apm accroding to README.md of the container.
```
rosrun gnc ctrl
```
