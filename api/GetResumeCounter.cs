using System.Net;
using System.Text.Json;
using Microsoft.Azure.Functions.Worker;
using Microsoft.Azure.Functions.Worker.Http;
using Microsoft.Extensions.Logging;

namespace Api.Function;

public class GetResumeCounter
{
    private readonly ILogger<GetResumeCounter> _logger;
    private readonly IResumeCounterService _resumeCounterService;

    public GetResumeCounter(ILogger<GetResumeCounter> logger, IResumeCounterService resumeCounterService)
    {
        _logger = logger;
        _resumeCounterService = resumeCounterService;
    }

    [Function("GetResumeCounter")]
    public async Task<UpdatedCounter> Run([HttpTrigger(AuthorizationLevel.Anonymous, "get", "post")] HttpRequestData req,
    [CosmosDBInput("DebarsheeAzureResume","Counter", Connection = "CosmosDbConnectionString", Id = "index",
            PartitionKey = "index")] Counter counter)
    {


        counter = _resumeCounterService.IncrementCounter(counter);

        var response = req.CreateResponse(HttpStatusCode.OK);
        response.Headers.Add("Content-Type", "application/json; charset=utf-8");
        string jsonString = JsonSerializer.Serialize(counter);
        await response.WriteStringAsync(jsonString);

        return new UpdatedCounter
        {
            NewCounter = counter,
            HttpResponse = response
        };
    }
}
