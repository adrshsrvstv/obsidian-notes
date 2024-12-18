- continuous - sometimes high volume data - like payments, stock trade data, sensor data, traffic data
- Stateful state processing:
	- record some intermediate data (such as count, total payment volume, etc) and not just do transformations
	- this "state" gets persisted
	- this is what we talk about
## Spark Streams:

- Uses micro batch - wait for some time, then process all packets till that time as a batch and process them in a distributed manner
	- process by batches, checkpoint, and repeat
		- secure - can go to last checkpoint
		- but, has a latency, because we have a wait, can't be instant (or in milliseconds) - is usually few seconds
- Structures Streaming Model:
	- data stream treated as an unbounded table with new records in stream treated as a new row in the table
	- use all the same batch processing APIs
	- keep appending the outputs of each batch operation to output table/stream
- So, steps involved:
	1. what's my input
	2. define transformation
	3. define output stream/sink
	4. **Imp**: specify things like checkpointing and processing details like when to trigger and when to process new data
	5. start the queries
- Transformation:
	- stateless: not dependent on previous data
	- stateful: like count, you need to maintain a state that needs to be communicated between plans
		- state is maintained in memory and frequently checkpointed to storage for fault tolerance
		- can be grouped into two classes:
			- aggregation not based on time - maybe based on count of input records etc
			- aggregation based on time - this is more challenging
- Aggregation based on time:
	- event time -  embedded in the data, which is when the event was created/triggered
		- decouples processing speed from output
		- deterministic despite failures
		- but we have to wait a bit to be sure we have received all events before a certain time
	- processing time - when event processed at server
		- easier to implement
		- but problematic in case of failures (??)
- Event time windows:
	- window of time by which I want my results aggregated
	- event can come at any time though - we process them by the event time and put them in the appropriate window
	- window can be overlapping too with say length of 10 minutes and sliding every 5 minutes - in this case results will be aggregated twice
		- can also read as `we want to count words within 10 minute windows, updating/sliding every 5 minutes
- But remember we keep the intermediate state data in memory - how long can we keep updating the old records?
	- Watermarks: the threshold of late data,  allows the engine to accordingly clean up old state. Late data within the threshold will be aggregated, but data later than the threshold will start getting dropped.
		- For a specific window ending at time `T`, the engine will maintain state and allow late data to update the state until `(max event time seen by the engine - late threshold > T)` - **Remember T is the state upper bound(12:05 or 12:10), not the event time (12:04)
		- **Remember that it is `max event time **seen by the engine**` and not the actual server time.**
		- So if the latest event time seen is 12:11, and watermark is 10 minutes, any state with upper bound time before 12:01 is flushed and no longer updated. 
		- Watermark threshold is updated every window update (`5 minutes` in above example of 10 minute windows) - not at every event receipt.
		- ![|750](attachments/Screenshot%202024-04-29%20at%203.03.50%20AM.png)

## Flink

