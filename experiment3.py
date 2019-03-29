import mortoray_path_finding as mpf
	
# maze = mpf.maze.create_empty_maze( 10, 10 )
# 	# [37,61,92,36] start, end/start, end/star, end which reverses to: [(7,3), (1,6), (2,9), (6,3)]
maze = mpf.maze.create_wall_maze_fixed( 10, 10 )

filled = mpf.tutorial_1.fill_shortest_path(maze.board, maze.start, maze.end)
path = mpf.tutorial_1.backtrack_to_start(filled, maze.end)
mpf.maze.block_path(filled, path)

mpf.maze.clear_pos(filled, [2,9])
filled2 = mpf.tutorial_1.fill_shortest_path_cont(filled,maze.end, [2,9] )
path2 = mpf.tutorial_1.backtrack_to_start(filled2, [2,9])
mpf.maze.block_path(filled, path2)


mpf.maze.clear_pos(filled, [6,3])
filled3 = mpf.tutorial_1.fill_shortest_path_cont(filled2, [2,9], [6,3]  )
path3 = mpf.tutorial_1.backtrack_to_start(filled3, [6,3])
# mpf.maze.block_path(filled, path2)



finder = mpf.draw.Finder()

finder.set_board(filled3)

finder.set_path(path3)

finder.run()

