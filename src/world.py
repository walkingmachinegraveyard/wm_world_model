#!/usr/bin/env python

from wm_world_model.srv import *
import yaml
import rospy


class world:

    def handle_knowledge(self, req):
        return "test"

    def parse_yaml(self):
        pass

    def world_knowledge_server(self):
        rospy.init_node('world_knowledge')
        print "123"
#        self.object_file = rospy.get_param("object_yaml")
#        self.person_file = rospy.get_param("person_yaml")

        self.s = rospy.Service('get_knowledge', GetKnowledge, self.handle_knowledge)
        rospy.spin()

if __name__ == "__main__":
    world = world()
    world.world_knowledge_server()
