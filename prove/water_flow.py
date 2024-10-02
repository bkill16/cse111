def water_column_height(tower_height, tank_height):
    height = tower_height + (3 * tank_height) / 4
    return height
    
def pressure_gain_from_water_height(height):
    pressure = (998.2 * 9.80665 * height) / 1000
    return pressure

def pressure_loss_from_pipe(pipe_diameter,
        pipe_length, friction_factor, fluid_velocity):
    negative_ff = friction_factor * -1
    velocity_sq = fluid_velocity ** 2
    lost_pressure = (negative_ff * pipe_length * 998.2 * velocity_sq) / (2000 * pipe_diameter)
    return lost_pressure