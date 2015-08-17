# Test script to generate an .osim file using specified input parameters to an existing model

import opensim
import inspect
import os
from opensim.opensim import ProbeSet
from sympy.integrals.heurisch import components

this_file_dir = os.path.dirname(
                os.path.abspath(inspect.getfile(inspect.currentframe())))

def test_check_env_var():
    if 'OPENSIM_HOME' not in os.environ:
        raise Exception("To run tests, must set environment "
                "variable OPENSIM_HOME "
                "to an OpenSim installation.")
        
def test_check_models_exist():
    if not os.path.isdir(os.environ["OPENSIM_HOME"] + "/Models"):
        raise Exception("To perform model demonstrations, it is"
                "necessary to have OpenSim models "
                "located in a 'Models' folder.")
        
def test_print_high_level_model_structure():
    
    # Create copy of the gait model.
    gait_model = opensim.Model(os.environ["OPENSIM_HOME"] + "/Models/Gait2392_Simbody/gait2392_simbody.osim")
    
    print("\nModel Structure:\n")
    
    print("<Model>")
    
    # Cycle through body sets and display body masses for each
    print("    <BodySet>")
    gait_body_set = gait_model.getBodySet()
    for reference in range(gait_body_set.getSize()):
        body = gait_body_set.get(reference)
        print("        <" + body.getName() + ">")
    print("    </BodySet>")
        
    # Cycle through constraints and display name for each
    print("    <ContraintSet>")
    gait_constraint_set = gait_model.getConstraintSet()
    for reference in range(gait_constraint_set.getSize()):
        constraint = gait_constraint_set.get(reference)
        print("        <" + constraint.getName() + ">")
    print("    </ConstraintSet>")
        
    # Cycle through force sets and display names of muscles for each
    print("    <ForceSet>")
    gait_force_set = gait_model.getForceSet()
    for reference in range(gait_force_set.getSize()):
        force = gait_force_set.get(reference)
        print("        <" + force.getName() + ">")
    print("    </ForceSet>")
    
    # Cycle through markers and display name for each
    print("    <MarkerSet>")
    gait_marker_set = gait_model.getMarkerSet()
    for reference in range(gait_marker_set.getSize()):
        marker = gait_marker_set.get(reference)
        print("        <" + marker.getName() + ">")
    print("    </MarkerSet>")
    
    # Cycle through contact geometry and display name for each
    print("    <ContactGeometrySet>")
    gait_contact_geometry_set = gait_model.getContactGeometrySet()
    for reference in range(gait_contact_geometry_set.getSize()):
        contact_geometry = gait_contact_geometry_set.get(reference)
        print("        <" + contact_geometry.getName() + ">")
    print("    </ContactGeometrySet>")
        
    # Cycle through controllers and display name for each
    print("    <ControllerSet>")
    gait_controller_set = gait_model.getControllerSet()
    for reference in range(gait_controller_set.getSize()):
        controller = gait_controller_set.get(reference)
        print("        <" + controller.getName() + ">")
    print("    </ControllerSet>")
    
    # Cycle through probes and display name for each
    print("    <ProbeSet>")
    gait_probe_set = gait_model.getProbeSet()
    for reference in range(gait_probe_set.getSize()):
        probe = gait_probe_set.get(reference)
        print("        <" + probe.getName() + ">")
    print("    </ProbeSet>")
        
    # Cycle through components and display name for each
    print("    <ComponentSet>")
    gait_component_set = gait_model.getMiscModelComponentSet()
    for reference in range(gait_component_set.getSize()):
        component = gait_component_set.get(reference)
        print("        <" + component.getName() + ">")
    print("    </ComponentSet>")
        
    print("</Model>\n")
    
def test_alter_existing_model_parameters():
    
    # Create copy of the gait model.
    gait_model = opensim.Model(os.environ["OPENSIM_HOME"] + "/Models/Gait2392_Simbody/gait2392_simbody.osim")
    
    # Extract Force Set for model
    force_set = gait_model.getForceSet()
    
    # Obtain reference to first muscle in set (glut_med1_r)
    muscles_set_gait = force_set.getMuscles()
    glut_med1_r = muscles_set_gait.get("glut_med1_r")
    
    # Get geometry path for muscle
    geom_path = glut_med1_r.getGeometryPath()
    
    # Get path point set from geometry path
    path_pt_set = geom_path.getPathPointSet()
    
    # Extract insertion point
    insertion_pt = path_pt_set.get("glut_med1_r-P2")
    
    # Examine current insertion point
    print("\nOld Insertion Point Coordinates:")
    print("x = " + str(insertion_pt.getLocationCoord(0)))
    print("y = " + str(insertion_pt.getLocationCoord(1)))
    print("z = " + str(insertion_pt.getLocationCoord(2)))
    
    # Define new insertion point
    insertion_pt.setLocationCoord(0, 0.00)
    insertion_pt.setLocationCoord(1, 0.00)
    insertion_pt.setLocationCoord(2, 0.00)
    
    # Print new insertion coordinates
    print("\nNew Insertion Point Coordinates")
    print("x = " + str(insertion_pt.getLocationCoord(0)))
    print("y = " + str(insertion_pt.getLocationCoord(1)))
    print("z = " + str(insertion_pt.getLocationCoord(2)))
    
    # Write changes to new file
    newName = os.path.join(this_file_dir, 'gait_altered_insertion_pt.osim')
    gait_model.printToXML(newName)
    
def test_create_muscle_tug_of_war_model():
    
    pass

def test_print_force_structure():
    
    # Create copy of the gait model.
    gait_model = opensim.Model(os.environ["OPENSIM_HOME"] + "/Models/Gait2392_Simbody/gait2392_simbody.osim")
    
    force_set = gait_model.getForceSet()
    force = force_set.get(1)
    variable_names = force.getStateVariableNames()
    print(variable_names.getSize())
    for reference in range(variable_names.getSize()):
        name = variable_names.get(reference)
        variable_value = name.getStateVariable(name)
        print(variable_value)    
    pass

def test_print_body_structure():

    # Create copy of the gait model.
    gait_model = opensim.Model(os.environ["OPENSIM_HOME"] + "/Models/Gait2392_Simbody/gait2392_simbody.osim")
    
    
    
    pass

def test_print_constraint_structure():
    
    # Create copy of the gait model.
    gait_model = opensim.Model(os.environ["OPENSIM_HOME"] + "/Models/Gait2392_Simbody/gait2392_simbody.osim")
    
    
    
    pass

def test_print_markers_structure():
    
    # Create copy of the gait model.
    gait_model = opensim.Model(os.environ["OPENSIM_HOME"] + "/Models/Gait2392_Simbody/gait2392_simbody.osim")
    
    
    
    pass

def test_print_contact_geometry_structure():
    
    # Create copy of the gait model.
    gait_model = opensim.Model(os.environ["OPENSIM_HOME"] + "/Models/Gait2392_Simbody/gait2392_simbody.osim")
    
    
    
    pass

def test_print_controllers_structure():
    
    # Create copy of the gait model.
    gait_model = opensim.Model(os.environ["OPENSIM_HOME"] + "/Models/Gait2392_Simbody/gait2392_simbody.osim")
    
    
    
    pass

def test_print_probe_structure():
    
    # Create copy of the gait model.
    gait_model = opensim.Model(os.environ["OPENSIM_HOME"] + "/Models/Gait2392_Simbody/gait2392_simbody.osim")
    
    
    
    pass

def test_print_components_structure():
    
    # Create copy of the gait model.
    gait_model = opensim.Model(os.environ["OPENSIM_HOME"] + "/Models/Gait2392_Simbody/gait2392_simbody.osim")
    
    
    
    pass
    
def main():
    test_check_env_var()
    test_check_models_exist()
    #test_print_high_level_model_structure()
    #test_alter_existing_model_parameters()
    #test_create_muscle_tug_of_war_model()
    #test_print_components_structure()
    #test_print_constraint_structure()
    #test_print_contact_geometry_structure()
    #test_print_controllers_structure()
    test_print_force_structure()
    #test_print_high_level_model_structure()
    #test_print_markers_structure()
    #test_print_probe_structure()
    #test_print_body_structure()

if __name__ == '__main__':
    main()