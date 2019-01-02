# based on https://uoftcoders.github.io/rcourse/lec07-pop-models.html
rm(list = ls(all.names = TRUE))
#dev.off()

library(ggplot2) 
#clears plots
#

N_seq <-
  seq(-2, 20,by=.01) # make a sequence of N values to plot dN/dt against

logistic_eqn <-  function(N, r, K) {
  # calculate dN/dt for the logistic equation
  
  # r: growth rate (divisions per hour) 
  # K: carrying capacity
  # N: population size
  return(r * N * (K - N ))
}

dN_dt <- logistic_eqn(N_seq, r = 1, K = 1)

qplot(N_seq, dN_dt) +
  geom_hline(aes(yintercept = 0)) # a line at zero for visual aid

# Example: deSolve with logistic eqn

# now we need to define our function a bit differently to be in the format that `ode` uses
logistic_fn <- function(t, state, parameters) {
  # Calculates dN/dt for the logistic equation
  
  # t: time point at which to evaluate derivative (doesn't actually change anything in this example)
  # state: vector of variables (here it's just N)
  # parameters: vector of model parameters c(r, K)
  
  N <- state 
  
  r <- parameters[1] # the first element of the parameters vector is r
  K <- parameters[2] # the second element of the parameters vector is K
  
  #rate of change
  dN <- r * N * (K - N )*(N-10*K)
  
  #return rate of change
  return(list(c(dN)))
}

parameters <- c(r = 1, K = 1)
state <- c(N = 2)
times <- seq(0, 50, by = 0.01) # the timestep dt is chosen by setting the increment with 'by'

#?ode # look at the documentation to learn about the parameters
result <- ode(y = state, times = times, func = logistic_fn, parms = parameters)
result <- data.frame(result) # convert it to a dataframe so we can use ggplot

ggplot(result) + geom_point(aes(x = time, y = N))


