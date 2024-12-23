```bash
(base) ➜  ~ docker stop lab1pre
lab1pre
(base) ➜  ~ docker exec -it lab1pre bash
ir@aef81bc83514:~$ DISPLAY=:1.0
ir@aef81bc83514:~$ export DISPLAY
ir@aef81bc83514:~$ echo $DISPLAY
:1.0
ir@aef81bc83514:~$ source devel/setup.bash
bash: devel/setup.bash: No such file or directory
ir@aef81bc83514:~$ cd catkin_ws/CS4278-5478-MotionPlanning/
ir@aef81bc83514:~/catkin_ws/CS4278-5478-MotionPlanning$ source devel/setup.bash
```