# Meetup demo
Just some notes about meetup demo that I'll be doing in few weeks.

## Used hardware
I'll be using my own virtual lab. I'm using vmware esxi host on HP Proliant
microserver gen 8

To reduce any network interuptions, I should bring my own server in place. But
then I would need some network switch with dhcp server to assign IP addresses.

After all, maybe it's better to let the server be in my place and connect
remotely.

## Content of demo

_note: infrastructure should be already created. I should have installed jenkins
or other CI server, prepared ssh keys, assigned keys in gitlab and so on_

* project is ready to start
* set up development machine
  * install vagrant
  * configure vagrant
  * use bootstrap
  * port forwading
  * running the application on vagrant

* set up gitlab CI to use runner to package application into python package
* set up gitlab CI to run coverage tests?
* set up gitlab CI to run unit tests?
* Trigger jenkins job
  * download package
  * deploy package on test server
* execute system tests
* execute some other tests
* create documentation
* create test report?
* if everything passes deploy on production server

