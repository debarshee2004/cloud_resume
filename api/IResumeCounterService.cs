namespace Api.Function;

public interface IResumeCounterService
{
    Counter IncrementCounter(Counter counter);
}

public class ResumeCounterService : IResumeCounterService
{
    public Counter IncrementCounter(Counter counter)
    {
        // Increment and return the counter
        counter.Count += 1;
        return counter;
    }
}