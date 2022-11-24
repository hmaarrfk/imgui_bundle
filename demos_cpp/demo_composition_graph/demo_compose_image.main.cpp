#include "functions_composition_graph/functions_composition_graph.h"
#include "functions_composition_graph/image_with_gui.h"
#include "imgui_bundle/imgui_bundle.h"
#include "imgui-node-editor/imgui_node_editor.h"

#include <opencv2/highgui.hpp>

int main(int, char**)
{
    using namespace VisualProg;

    cv::Mat image = cv::imread("resources/house.jpg");
    cv::resize(image, image, cv::Size(), 0.5, 0.5);

    auto split_lut_merge_gui = Split_Lut_Merge_WithGui(ColorType::BGR);

//    std::vector<FunctionWithGuiPtr> functions {
//        std::make_shared<SplitChannelsWithGui>(),
//        std::make_shared<LutChannelsWithGui>(),
//        std::make_shared<MergeChannelsWithGui>(),
//    };

    std::vector<FunctionWithGuiPtr> functions {
        split_lut_merge_gui._split, split_lut_merge_gui._lut, split_lut_merge_gui._merge};

    FunctionsCompositionGraph compositionGraph(functions);
    compositionGraph.SetInput(image);

    auto gui = [&](){
        compositionGraph.Draw();
    };

    ImGuiBundle::AddOnsParams addOnsParams;
    ax::NodeEditor::Config nodeEditorConfig;
    nodeEditorConfig.SettingsFile = "demo_compose_image.json";

    addOnsParams.withNodeEditorConfig = nodeEditorConfig;
    HelloImGui::SimpleRunnerParams params;
    params.guiFunction = gui;
    params.windowSize = {1600, 1000};
    ImGuiBundle::Run(params, addOnsParams);

    return 0;
}