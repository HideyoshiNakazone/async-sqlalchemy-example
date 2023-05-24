# Simple Async SQLAlchemy Example

## Example Results

```
Async time:  0:00:50.757666
Regular time:  0:02:29.770093
```
Ran with 100k records each with 100kb of data for a total of 10GB of data per method.
Each stream of data is partitioned into 1000 records per transaction.

The test was ran with a local database on a SSD and a Ryzen 9 7950x.

## Conclusion

When inserting into a database a large and heavy stream of data it's best to use the async method. This will allow the program to continue running while the database is being written to. This is especially useful when the database is on a different server or in the cloud. The regular method will block the program from running until the database is finished writing. This is not ideal for large amounts of data.
