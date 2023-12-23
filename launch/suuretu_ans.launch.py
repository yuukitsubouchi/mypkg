# SPDX-FileCopyrightText: 2023 Yuuki Tsubouchi 　　　　　
# SPDX-License-Identifier: BSD-3-Clause
import launch
import launch.actions
import launch.substitutions
import launch_ros.actions


def generate_launch_description():

    suuretu = launch_ros.actions.Node(
        package='mypkg',
        executable='suuretu',
        )
    ans = launch_ros.actions.Node(
        package='mypkg',
        executable='ans',
        output='screen'
        )

    return launch.LaunchDescription([suuretu, ans])
