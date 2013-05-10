//
//  main.m
//  count to 50 billion
//
//  Created by Philipp on 10. 05. 13. (Germany)
//
//  CC Lisense: Attribution-NonCommercial-ShareAlike 3.0 Unported
//  For comercial usage just ask, may I grant you ;-)
//
//
// According to Apple it would take up to 1600 Years to count 50 billion. Well lets see how long it takes on a Mac OS X machine ;-)
// Source: Apples "50 billion App Downloads" advertising campaign

#import <Foundation/Foundation.h>

int Count(unsigned long int NumberToCountUpTo);

int main(int argc, const char * argv[])
{
    
    @autoreleasepool {
        
        unsigned long int NumberToCountUpTo = 50000000000;
        unsigned int Response;
        
        NSLog(@"Started..."); // Start message
        
        NSDate *methodStart = [NSDate date];

        Response = Count(NumberToCountUpTo);
        
        NSDate *methodFinish = [NSDate date];
        NSTimeInterval executionTime = [methodFinish timeIntervalSinceDate:methodStart];
        
        NSLog(@"Ended: it tok: %f", executionTime); // End message
        /*
        So, now we know this takes quite a few sekonds costs about 1%% of battery life, and spams the RAM. All in all we kan say this was realy useless BUT Funy!
         */
    }
    return 0;
}

int Count(unsigned long int NumberToCountUpTo)
{
    unsigned int Counter;
 
    for (Counter = 0; Counter < NumberToCountUpTo; Counter++) {
        printf("Now at: %d\n", Counter);
    }
    
    return 0;
}
