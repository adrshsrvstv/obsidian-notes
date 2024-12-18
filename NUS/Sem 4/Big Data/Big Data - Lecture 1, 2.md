
- Challenges of Big data:
	- volume - massive datasets
	- variety - image, text, video, tweets
	- velocity - of sensor or trade data or network data - DRAM limits after a point
	- veracity - or uncertainty of data - mislabelled data

- Storage:
	- Server --(rack switch)-> Rack --(datacenter switch)-> Cluster
- Bandwidth, latency, and throughput:
	- Bandwidth: how wide the road/lane is - how many packets per second CAN be transmitted - maximum amount of data that can be transmitted per unit time (e.g. in GB/s)
	- Latency: trip time for 1 packet - time taken for 1 packet to go from source to destination (one-way) or from source to destination back to source (round trip), e.g. in ms
	- Throughput: how many packets per second ACTUALLY transmitted
- In calculations:
	- total bandwidth = min(individual bandwidths), because that is the bottleneck
	- total latency = sum(individual latencies)
- Some typical values (latency, bandwidth):
	- DRAM = 100nanosec, 20GBps
	- Disk: 10milisec, 200MBps
	- rack switch: 300 microsec, 100MBps
	- datacenter switch: 500microsec, 10mbps
- Sample calculations:
	- DRAM another machine: sum(100ns, 300microsec) = ~ 300 microsec; min(100mbps, 20gbps)= 100mbps
	- Disk another machine: sum(10ms, 300microsec) = ~ 10 ms; min(100mbps, 200MBps)= 100mbps
	- DRAM another rack: sum(100ns, 300micros **\* 2**,  500 micros) (***because 2 racks involved***) = ~1100 micros; min(20gbps, 100mbps, 10mbps) = 10mpbs
	- Disk another rack: sum(10ms, 300micros **\* 2**,  500 micros) (***because 2 racks involved***) = ~10ms; min(200mbps, 100mbps, 10mbps) = 10mpbs


- 4 big ideas: 
	- scale out, not up: horizontally add more machines, instead of upgrading to higher spec machines. cuz cheap plus redundancy
	- seamless scalability: overheads should be negligible - scale processing linearly with # of machines
	- move processing to data: to avoid overheads
	- avoid random access, access data sequentially: seeks are expensive
- 3 big challenges:
	- machine failures
	- synchronization
	- programming complexity - because concurrency at datacenter scale is hard to reason