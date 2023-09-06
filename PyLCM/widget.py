# user_parameters.py
# functions for input and output
import numpy as np
import ipywidgets as widgets
from IPython.display import display, clear_output

# initialization functions: displays widgets and reads in parameters given by the user
def model_steering_input():
    # Adjust the style that descriptions are displayed in full length
    style = {'description_width': 'initial'}
    
    # Create the widgets for the variables
    dt_widget      = widgets.BoundedFloatText(description='dt [s]:', min = 0.0001, max = 5.0, value = 0.5, style=style)
    nt_widget      = widgets.IntText(description='nt:', value = 3600, style=style)

    Condensation_widget = widgets.Checkbox(description='Condensation:', value=True, style=style)
    Collision_widget = widgets.Checkbox(description='Collision:', value=False, style=style)

    n_particles_widget = widgets.BoundedIntText(description='n_particles:', min=100, max=1000, value=500, style=style)
   
    max_z_widget = widgets.BoundedFloatText(description='z_max [m]:', min = 0.0, max = 2000.0, step = 0.1, value=1500.0, style=style)
    # max value of collision_start_t_widget not updated when nt changed in the textbox! It remains at the default value of nt_widget
    
    z_widget = widgets.BoundedFloatText(description='z_0 [m]:', min = 0.0, max = 800.0, step = 0.1, value=0.0, style=style)

    # Display the widgets
    display('Model steering parameters',dt_widget, nt_widget, Condensation_widget,Collision_widget, n_particles_widget, max_z_widget) 
    
    return dt_widget, nt_widget, Condensation_widget, Collision_widget, n_particles_widget, max_z_widget
def parcel_info_input():
    style = {'description_width': 'initial'}
    # section for widgets for parcel info
    T_widget = widgets.BoundedFloatText(description='T [K]:', min = 200.0, max = 320.0, step = 0.1, value=293.2, style=style)
    P_widget = widgets.BoundedFloatText(description='P [Pa]:', min = 950.0E2, max = 1050.0E2, step = 1, value=1013.0E2, style=style)
    RH_widget= widgets.BoundedFloatText(description='RH [-]:', min = 0.01, max = 0.99, step = 0.01, value=0.88, style=style)
    w_widget = widgets.BoundedFloatText(description='w [m/s]:', min = 0.0, max = 10, step = 0.1, value=0.5, style=style)
    z_widget = widgets.BoundedFloatText(description='z [m]:', min = 0.0, max = 20000.0,  step = 100.0, value=0.0, style=style)


    # Display widgets
    display('Parcel initial parameters: ', T_widget, P_widget, RH_widget, w_widget, z_widget)
    
    return T_widget, P_widget, RH_widget, w_widget, z_widget

def ascending_mode_input():
    # user can choice the ascending mode
    ascending_mode_widget = widgets.ToggleButtons(options=['linear', 'sine', 'in_cloud_oscillation'], value='linear', description='Mode', layout={'width': 'max-content'}, disabled=False)
    display(ascending_mode_widget)
    # maybe include more advanced ascending modes later
    
    return ascending_mode_widget

def aero_mode_input():
    # widgets for aerosol initialisation
    mode_aero_init_widget = widgets.ToggleButtons(options=['weighting_factor', 'random'], value='weighting_factor', layout={'width': 'max-content'}, disabled=False)

    # Display widgets
    display('Aerosol initialisation mode: ', mode_aero_init_widget)
    
    return mode_aero_init_widget

# initialization function for the grid widget for aerosol modes
def grid_modes_input():
    # N, mu, sigma for each mode
    # widgets in GridspecLayout
    # see: https://ipywidgets.readthedocs.io/en/latest/examples/Layout%20Templates.html#style-attributes
    #print('Click on the heading buttons to plot the distributions of the respective modes. (Plot functionality will be added later)')
    print('N_aero: number of aerosols per cubic centimeter, mu: mean droplet radius, sigma: std of mu')

    # Arrange the widgets in a 4x4 layout
    gridwidget = widgets.GridspecLayout(4, 4)
    
    # Adjust the style that descriptions are displayed in full length
    style = {'description_width': 'initial'}

   
    # col 0 for mode 1
    gridwidget[0, 0]= widgets.Button(description='Mode #1', disabled=False, button_style='info', tooltip='Heading', style=style)
    # idea: print distribution on clicking
    # see: https://ipywidgets.readthedocs.io/en/latest/examples/Widget%20List.html#button
    gridwidget[1, 0] = widgets.BoundedFloatText(description='N_aero[cm⁻3]', min = 0.0, max = 5000.0, step = 0.1, value=1000.0, style=style)
    # internally multiply this by 1E6
    gridwidget[2, 0] = widgets.BoundedFloatText(description='mu [µm]', min = 0.0, max = 5.0, step = 0.001, value=0.008, style=style)
    # internally multiply this by 1E-6 and take the log
    gridwidget[3, 0] = widgets.BoundedFloatText(description='sigma [-]', min = 0.0, max = 3.0, step = 0.1, value=1.6, style=style)
    # internally take the log

    # col 1 for mode 2
    gridwidget[0, 1]= widgets.Button(description='Mode #2', disabled=False, button_style='info', tooltip='Heading')
    gridwidget[1, 1] = widgets.BoundedFloatText(description='N_aero[cm⁻3]', min = 0.0, max = 5000.0, step = 0.1, value=800.0, style=style)
    # internally multiply this by 1E6
    gridwidget[2, 1] = widgets.BoundedFloatText(description='mu [µm]', min = 0.0, max = 5.0, step = 0.001, value=0.034, style=style)
    # internally multiply this by 1E-6 and take the log
    gridwidget[3, 1] = widgets.BoundedFloatText(description='sigma [-]', min = 0.0, max = 3.0, step = 0.1, value=2.1, style=style)
    # internally take the log

    # col 2 for mode 3
    gridwidget[0, 2]= widgets.Button(description='Mode #3', disabled=False, button_style='info', tooltip='Heading')
    gridwidget[1, 2] = widgets.BoundedFloatText(description='N_aero[cm⁻3]', min = 0.0, max = 5000.0, step = 0.01, value=0.72, style=style)
    # internally multiply this by 1E6
    gridwidget[2, 2] = widgets.BoundedFloatText(description='mu [µm]', min = 0.0, max = 5.0, step = 0.1, value=0.46, style=style)
    # internally multiply this by 1E-6 and take the log
    gridwidget[3, 2] = widgets.BoundedFloatText(description='sigma [-]', min = 0.0, max = 3.0, step = 0.1, value=2.2, style=style)
    # internally take the log


    # col 3 for mode 4
    gridwidget[0, 3]= widgets.Button(description='Mode #4', disabled=False, button_style='info', tooltip='Heading')
    gridwidget[1, 3] = widgets.BoundedFloatText(description='N_aero[cm⁻3]', min = 0.0, max = 5000.0, step = 0.1, value=0, style=style)
    # internally multiply this by 1E6
    gridwidget[2, 3] = widgets.BoundedFloatText(description='mu [µm]', min = 0.0, max = 5.0, step = 0.1, value=0, style=style)
    # internally multiply this by 1E-6 and take the log
    gridwidget[3, 3] = widgets.BoundedFloatText(description='sigma [-]', min = 0.0, max = 3.0, step = 0.1, value=0, style=style)
    # internally take the log


    # additional button in the end for the cumulative distr.
    # to be added later when plot of the aerosol distribution is working
    # plotbutton_widget = widgets.Button(description='Plot cumulative distr.', disabled=False, button_style='info', tooltip='Plot cumulative distribution of all modes')

    display(gridwidget)
    # display(plotbutton_widget)
    
    return gridwidget



# function for kohler activation radius widget
def kohler_settings():
    # Adjust the style that descriptions are displayed in full length
    style = {'description_width': 'initial'}
    # set if activation radius uses kohler critical radius
    kohler_widget = widgets.Checkbox(description='Set activation radius using Koehler critical radius.', value=False, style=style, layout={'width': 'max-content'})
    # display
    display(kohler_widget)
     
    return kohler_widget



# function for time step widgets
def timestep_display_mode_settings():
    # setting of display mode while running: either output of variables in text form (fast, recommended) = 'text'
    # or: continuously updated plot using plotly (slower, memory consuming) = 'graphics'
    mode_displaytype_widget = widgets.ToggleButtons(options=['text_fast', 'graphics'], value='graphics', layout={'width': 'max-content'}, disabled=False)
    display('Display mode: ', mode_displaytype_widget)
    
    return mode_displaytype_widget

# function for plot widgets
def plot_widgets_settings(nt):
    # user can choice if he wants the plots time-dependent or height-dependent (except of DSD and particle densities always being time dependent)
    # Adjust the style that descriptions are displayed in full length
    style = {'description_width': 'initial'}
    mode_plots_widget = widgets.ToggleButtons(options=['time-series', 'vertical profile'], value='time-series', description='Plots are:', layout={'width': 'max-content'}, disabled=False, style=style)
    # Widget to set in which increment lines for the spectra are drawn
    increment_widget = widgets.BoundedIntText(description='For droplet spectra: increment: ', value=20, min = 1, max = nt, step=1, style=style)
    
    # display the widgets
    display(mode_plots_widget, 'For droplet spectra: set increment (e.g. 20: every 20th timestep a line is drawn): ', increment_widget)
    
    return mode_plots_widget, increment_widget