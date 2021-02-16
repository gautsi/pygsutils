# Caching

I often have to prepare data before analysis, and this can get complicated with many steps. One way I try to handle this complexity is to break up the prep process into many small functions, one for each step, each taking a dataframe from the previous step and sending a modified dataframe on to the next. Ideally I want for debug purposes to be able to at least spot check the data after each step, and for efficiency purposes not to have to rerun all steps after changing a step or after stopping the process and resuming later. In other words I want to cache the data after each step, ideally in a way that
- saves the data as csv files for ease of spot checking,
- is persistent across kernel restarts, and
- doesn't require a lot of boilerplate code.

Inspired by [diskcache](http://www.grantjenks.com/docs/diskcache/index.html), the cache module implements a simple dataframe cacher that caches dataframes as csvs to disk. 