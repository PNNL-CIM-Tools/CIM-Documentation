zenuml
    title BlazegraphConnection
    @Actor User
    @PubSub GraphModel
    @AzureFunction ConnectionInterface
    @AzureBackup Blazegraph_DB

    @Starter(User)
    // `Initialization`
    ConnectionInterface.BlazegraphConnection() {
        Blazegraph_DB.connect() {
            return SPARQLWrapper
        }
        return
    }