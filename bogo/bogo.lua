function bogosort ()
    math.randomseed(os.time())
    io.write("Welcome to BogoSort in Lua!")
    io.write("Please enter the number of integers you would like to sort:\n")
    size = io.read()
    list = {}
    -- Lua issue "workaround"
    math.random(100)
    for i=0, size do
        list[i] = math.random(10)
    end 
    -- if type (list) ~= 'table' then return list end
 
    -- Fisher-Yates Knuth shuffle
    local function shuffle ()
        local rand = math.random(1,#list)
        for i=1,#list do
            list[i],list[rand] = list[rand],list[i]
            rand = math.random(1,#list)
        end
    end
 
    -- Returns true only if list is now sorted
    local function in_order ()
        local last = list[1]
        for i,v in next,list do
            if v < last then return false end
            last = v
        end
        return true
    end
 
    while not in_order() do shuffle() end
 
    return list
end
