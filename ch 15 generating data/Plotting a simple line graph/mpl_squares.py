import matplotlib.pyplot as plt #number of functions that generate charts and plots

squares = [1, 4, 9, 16, 25]

fig, ax = plt.subplots() #subplot() - generate 1 or more plots in same figure 
                    #fig - represents the entire figure or collection of plots that are generated
ax.plot(squares) #axvariable represents a single plot in figure
    #plot - plots given info
plt.show() #opens Matplotlib's viewer