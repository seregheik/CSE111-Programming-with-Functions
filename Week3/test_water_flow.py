from pytest import approx
import pytest
from water_flow import (water_column_height,
                        pressure_gain_from_water_height,
                        pressure_loss_from_pipe,
                        pressure_loss_from_fittings,
                        reynolds_number,
                        pressure_loss_from_pipe_reduction)
def test_water_column_height():
    assert water_column_height(0.0,0.0) == 0.0
    assert water_column_height(0.0, 10.0) == 7.5
    assert water_column_height(25.0, 0.0) == 25.0
    assert water_column_height(48.3, 12.8) == 57.9
def test_pressure_gain_from_water_height():
    assert pressure_gain_from_water_height(0.0) == approx(0.000, abs=0.001)
    assert pressure_gain_from_water_height(30.2) == approx(295.628, abs=0.001)
    assert pressure_gain_from_water_height(50.0) == approx(489.450, abs=0.001)
def test_pressure_loss_from_pipe():
    assert (
            pressure_loss_from_pipe(
                pipe_diameter=0.048692,
                pipe_length=0.00,
                friction_factor=0.018,
                fluid_velocity=1.75
            ) == approx(0.000, abs=0.001)
    )
    assert (
            pressure_loss_from_pipe(
                pipe_diameter=0.048692,
                pipe_length=200.00,
                friction_factor=0.000,
                fluid_velocity=1.75
            ) == approx(0.000, abs=0.001)
    )
    assert (
            pressure_loss_from_pipe(
                pipe_diameter=0.048692,
                pipe_length=200.00,
                friction_factor=0.018,
                fluid_velocity=0.00
            ) == approx(0.000, abs=0.001)
    )
    assert (
            pressure_loss_from_pipe(
                pipe_diameter=0.048692,
                pipe_length=200.00,
                friction_factor=0.018,
                fluid_velocity=1.75
            ) == approx(-113.008, abs=0.001)
    )
    assert (
            pressure_loss_from_pipe(
                pipe_diameter=0.048692,
                pipe_length=200.00,
                friction_factor=0.018,
                fluid_velocity=1.65
            ) == approx(-100.462, abs=0.001)
    )
    assert (
            pressure_loss_from_pipe(
                pipe_diameter=0.286870,
                pipe_length=1000.00,
                friction_factor=0.013,
                fluid_velocity=1.65
            ) == approx(-61.576, abs=0.001)
    )
    assert (
            pressure_loss_from_pipe(
                pipe_diameter=0.286870,
                pipe_length=1800.75,
                friction_factor=0.013,
                fluid_velocity=1.65
            ) == approx(-110.884, abs=0.001)
    )
def test_pressure_loss_from_fittings():
    assert  pressure_loss_from_fittings(
        fluid_velocity=0.00,
        quantity_fittings=3
    ) == approx(0.000, abs=0.001
                )
    assert pressure_loss_from_fittings(
        fluid_velocity=1.65,
        quantity_fittings=0
    ) == approx(0.000, abs=0.001
                )
    assert pressure_loss_from_fittings(
        fluid_velocity=1.65,
        quantity_fittings=2
    ) == approx(-0.109, abs=0.001
                )
    assert pressure_loss_from_fittings(
        fluid_velocity=1.75,
        quantity_fittings=2
    ) == approx(-0.122, abs=0.001
                )
    assert pressure_loss_from_fittings(
        fluid_velocity=1.75,
        quantity_fittings=5
    ) == approx(-0.306, abs=0.001
                )
def test_reynolds_number():
    assert reynolds_number(
        hydraulic_diameter=0.048692,
        fluid_velocity=0.00) == approx(0, abs=1
                                       )

    assert reynolds_number(
        hydraulic_diameter=0.048692,
        fluid_velocity=1.65) == approx(80069, abs=1
                                       )

    assert reynolds_number(
        hydraulic_diameter=0.048692,
        fluid_velocity=1.75) == approx(84922, abs=1
                                       )

    assert reynolds_number(
        hydraulic_diameter=0.286870,
        fluid_velocity=1.65) == approx(471729, abs=1
                                       )

    assert reynolds_number(
        hydraulic_diameter=0.286870,
        fluid_velocity=1.75) == approx(500318, abs=1
                                       )
def test_pressure_loss_from_pipe_reduction():
    assert pressure_loss_from_pipe_reduction(
        larger_diameter = 0.28687,
        fluid_velocity = 0.00	,
        reynolds_number = 1,
        smaller_diameter= 0.048692
    ) == approx(0.000, abs=0.001)

    assert pressure_loss_from_pipe_reduction(
        larger_diameter=0.28687,
        fluid_velocity=1.65,
        reynolds_number=471729,
        smaller_diameter=0.048692
    ) == approx(-163.744, abs=0.001)

    assert pressure_loss_from_pipe_reduction(
        larger_diameter=0.28687,
        fluid_velocity=1.75,
        reynolds_number=500318,
        smaller_diameter=0.048692    ) == approx(-184.182, abs=0.001)


pytest.main(['-v', '--tb=line','-rN', __file__])