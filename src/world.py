#!/usr/bin/env python

from wm_world_model.srv import GetKnowledge
from wm_world_model.msg import world_person, world_object
from std_msgs.msg import String, Int8, Float32

import yaml
import rospy


class world:

    def handle_knowledge(self, req):
        self.parse_yaml()

        return self.object_array, self.person_array

    def parse_yaml(self):
        with open(self.object_file, 'r') as o:
            try:
                self.object_yml = yaml.load(o)
                for item, data in self.object_yml.iteritems():
                    msg = world_object()
                    rospy.logout(data)
                    msg.world_id = data["world_id"]
                    msg.ork_id = data["ork_id"]
                    msg.object_name = data["object_name"]
                    msg.type = data["type"]
                    msg.color = data["color"]
                    msg.x = data["x"]
                    msg.y = data["y"]
                    msg.z = data["z"]
                    self.object_array.append(msg)
            except yaml.YAMLError as exc:
                print(exc)

        with open(self.person_file, 'r') as p:
            try:
                self.person_yml = yaml.load(p)
                for item1, data1 in self.person_yml.iteritems():
                    rospy.loginfo(self.person_yml)
                    msg = world_person()
                    rospy.loginfo(data1)
                    msg.world_id = data1["world_id"]
                    msg.name = data1["name"]
                    msg.sex = data1["sex"]
                    msg.action = data1["action"]
                    msg.x = data1["x"]
                    msg.y = data1["y"]
                    msg.z = data1["z"]
                    self.person_array.append(msg)
            except yaml.YAMLError as exc:
                print(exc)

    def world_knowledge_server(self):
        rospy.init_node('world_knowledge')
        self.object_array = []
        self.person_array = []
        self.object_file = rospy.get_param('object_yml')
        self.person_file = rospy.get_param('person_yml')

        self.knowledge_service = rospy.Service(
            'world/get_knowledge', GetKnowledge, self.handle_knowledge
        )
        rospy.spin()


if __name__ == "__main__":
    world = world()
    world.world_knowledge_server()
